void setup() {
  // put your setup code here, to run once:

}

void loop() { 
  // if(digitalRead(A10)>200)
  //   digitalWrite(A6,High)
  // }
  analogWrite(13, 255); // sets the LED on
  digitalWrite(A6,HIGH);
  digitalWrite(A7,LOW);
  delay(3000);                // waits for a second (1000 ms)
  int sensorValue = digitalRead(A6); // Read analog pin A0
  Serial.println(sensorValue);      // Print value to Plotter
  analogWrite(13, 0);  // sets the LED off
  digitalWrite(A6,LOW);
  digitalWrite(A7,HIGH)
  // delay(3000);
  // sensorValue = digitalRead(A6); // Read analog pin A0
  // Serial.println(sensorValue);      // Print value to Plotter
}
