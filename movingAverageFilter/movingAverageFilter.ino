// Definitions
#define EMG_PIN_CH1     A0        
#define EMG_PIN_CH2     A1        
#define SAMPLE_RATE_HZ  1000
#define WINDOW_SIZE     50
#define ADC_RESOLUTION  12

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

uint32_t lastSampleTime = 0;
const uint32_t SAMPLE_INTERVAL_US = 1000000 / SAMPLE_RATE_HZ;

// Setup Code

void setup() {
    Serial.begin(115200);
    analogReadResolution(ADC_RESOLUTION);
    analogReadAveraging(4);

    pinMode(EMG_PIN_CH1, INPUT);
    pinMode(EMG_PIN_CH2, INPUT);
    pinMode(13, OUTPUT);
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
            if (ch1.isActive()) digitalWrite(13,HIGH);
            else digitalWrite(13,LOW);
            // processEMGSignal(ch1, ch2);
        }
    }
}