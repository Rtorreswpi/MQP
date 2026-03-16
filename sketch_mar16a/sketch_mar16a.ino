void setup() {
  // put your setup code here, to run once:

}

void loop() { 
  analogWrite(13, 255); // sets the LED on
  digitalWrite(A6,HIGH);
  delay(3000);                // waits for a second (1000 ms)
  int sensorValue = digitalRead(A6); // Read analog pin A0
  Serial.println(sensorValue);      // Print value to Plotter
  analogWrite(13, 0);  // sets the LED off
  digitalWrite(A6,LOW);
  delay(3000);
  sensorValue = digitalRead(A6); // Read analog pin A0
  Serial.println(sensorValue);      // Print value to Plotter
}
