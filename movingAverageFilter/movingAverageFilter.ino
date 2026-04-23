// Definitions
#define EMG_PIN_CH1     A0        
#define EMG_PIN_CH2     A1        
#define SAMPLE_RATE_HZ  1000
#define WINDOW_SIZE     50
#define ADC_RESOLUTION  12
#define EEG_PIN            A2
#define WINDOW_US 1000000  // 1 second
#define THRESHOLD         50
// #define MIN_PEAK_SPACING   1//ms (prevents double counting)
#define EXPECTED_PEAKS     6//max peaks expected in a second

//vars
int prev = 0;
int curr = 0;

int peakcount = 0;
uint32_t windowStart = 0;

uint32_t lastSampleTime = 0;
uint32_t lastPeakTime = 0;
uint32_t lastWindowTime = 0;

float dt = 0.001;   // 1 kHz

// High-pass
float RC_high = 0.1;//set to 61hz
float a_high;

// Low-pass
float RC_low = 0.01;//set to 59hz
float a_low;

// State variables
float prevInput = 0.0;
float prevHigh = 0.0;
float prevLow = 0.0;


// Moving Average Filter
class MovingAverageFilter {
private:
    float    buffer[WINDOW_SIZE];
    int      head;
    float    sum;
    int      count;
    bool     bufferFull;

public:
    MovingAverageFilter() : head(0), sum(0.0f), count(0), bufferFull(false) {memset(buffer, 0, sizeof(buffer));
    }

    float update(float newSample) {
        sum -= buffer[head];
        buffer[head] = newSample;
        sum += newSample;
        head = (head + 1) % WINDOW_SIZE;
        if (count < WINDOW_SIZE) { count++; } else { bufferFull = true; }
        return sum / count;
    }

    void reset() {
        memset(buffer, 0, sizeof(buffer));
        head = 0; sum = 0.0f; count = 0; bufferFull = false;
    }

    bool  isReady()    const { return bufferFull; }
    float getAverage() const { return (count > 0) ? sum / count : 0.0f; }
};

// EMG Channels
struct EMGChannel {
    const char*         name;
    int                 pin;
    MovingAverageFilter filter;
    float               rawValue;
    float               filteredValue;
    float               threshold;

    EMGChannel(const char* n, int p, float t)
        : name(n), pin(p), rawValue(0.0f), filteredValue(0.0f), threshold(t) {}

    void sample() {
        rawValue      = (float)analogRead(pin) / (float)((1 << ADC_RESOLUTION) - 1); filteredValue = filter.update(rawValue);
    }

    bool isActive() const { return filteredValue > threshold; }
    bool isReady()  const { return filter.isReady(); }
};
//biceps 0.1f, triceps 0.04f
EMGChannel ch1("Biceps",   EMG_PIN_CH1, 0.1f); //change the third variable for active.
EMGChannel ch2("Triceps", EMG_PIN_CH2, 0.08f); //change the third variable for active. 

const uint32_t SAMPLE_INTERVAL_US = 1000000 / SAMPLE_RATE_HZ;

// Setup Code

void setup() {
    Serial.begin(115200);
    analogReadResolution(ADC_RESOLUTION);
    analogReadAveraging(4);

    pinMode(EMG_PIN_CH1, INPUT);
    pinMode(EMG_PIN_CH2, INPUT);
    // pinMode(13, OUTPUT); LED
    a_high = RC_high / (RC_high + dt);
    a_low  = dt / (RC_low + dt);
    pinMode(A6, OUTPUT);//emg
    pinMode(A7, OUTPUT);

    pinMode(A8,OUTPUT);//eeg
    pinMode(A9,OUTPUT);

    digitalWrite(A6, LOW);  // idle
    digitalWrite(A7, LOW);
    digitalWrite(A8, LOW);
    digitalWrite(A9, LOW);
}

bool inpeak = false;

bool detectPeak(int curr) {
    bool isAbove = curr > THRESHOLD;
    
    if (isAbove && !inpeak) {
        inpeak = true;
        return true;   // rising edge → count peak
    }
    else if (!isAbove && inpeak) {
        inpeak = false; // reset when signal drops
    }

    return false;
}
// Main Loop

void loop() {
    uint32_t now = micros();

    if ((now - lastSampleTime) >= SAMPLE_INTERVAL_US) {
        lastSampleTime = now;

        ch1.sample();
        ch2.sample();

        Serial.print(ch1.rawValue, 4);      Serial.print(",");
        Serial.print(ch1.filteredValue, 4); Serial.print(",");
        Serial.print(ch2.rawValue, 4);      Serial.print(",");
        Serial.println(ch2.filteredValue, 4);

        if (ch1.isReady() && ch2.isReady()) {
            if (ch1.isActive()) {
                digitalWrite(A6,HIGH);
                digitalWrite(A7, LOW);
            }
            // else if (ch2.isActive()){
            //     digitalWrite(A7,HIGH);
            //     digitalWrite(A6, LOW);
            // }
            else {
                digitalWrite(A6, LOW);
                digitalWrite(A7, LOW);
            }
            // processEMGSignal(ch1, ch2);
        }

    }
 // --- EEG sampling (runs every loop, non-blocking) ---
int signal = analogRead(EEG_PIN);

// High-pass
float high = highpass(a_high, prevHigh, signal, prevInput);

// Low-pass
float low = lowpass(prevLow, a_low, high);

prevInput = signal;
prevHigh = high;
prevLow = low;

// Detect peaks
if (detectPeak(low)) {
    peakcount++;
}

// --- Window timing (1 second) ---
if (micros() - windowStart >= WINDOW_US) {
    Serial.println(peakcount);

    if (peakcount > EXPECTED_PEAKS) {
        digitalWrite(A8, HIGH);
        digitalWrite(A8, LOW);
    } else {
        digitalWrite(A8, LOW);
        digitalWrite(A9, HIGH);
    }

    peakcount = 0;               // reset for next window
    windowStart = micros();      // restart window
}
}
float highpass(float a_high, float prevHigh, float input, float prevInput){
  return a_high * prevHigh + a_high * (input - prevInput);
}
float lowpass(float prevLow, float a_low, float high){
  return prevLow + a_low * (high - prevLow);
}