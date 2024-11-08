#define svecha 3

void setup(){
  pinMode(svecha, OUTPUT);
}

void loop(){
  digitalWrite(svecha, 1);
  delay(10000);
  digitalWrite(svecha, 0);
  delay(10000);
}