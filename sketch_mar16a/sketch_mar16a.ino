void setup() {
  pinMode(A6, OUTPUT);
  pinMode(A7, OUTPUT);

  digitalWrite(A6, HIGH);  // idle
  digitalWrite(A7, HIGH);
}

void loop() {
  digitalWrite(A6, LOW);   // trigger
  digitalWrite(A7, HIGH);   // trigger
  delay(1000);
  digitalWrite(A6, HIGH);
  digitalWrite(A7, LOW);   // trigger

  delay(1000);
}