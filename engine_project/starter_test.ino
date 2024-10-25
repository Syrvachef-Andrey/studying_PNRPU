// #define RPWM 3
// #define LPWM 5
// #define REN 2
// #define LEN 4
// #define RIS 7
// #define LIS 6

// void setup()
// {
//   pinMode(RPWM, 1);
//   pinMode(LPWM, 1);
//   pinMode(REN, 1);
//   pinMode(LEN, 1);
//   pinMode(RIS, 1);
//   pinMode(LIS, 1);
//   digitalWrite(REN, 1);
//   digitalWrite(LEN, 1);
//   digitalWrite(RIS, 0);
//   digitalWrite(LIS, 0);
// }

// void loop()
// {
//   digitalWrite(RPWM, 150);
//   delay(3000);
//   digitalWrite(RPWM, 0);
//   delay(3000);
// }

   /*
  BTS7960-43A-Driver
  made on 22 Nov 2020
  by Amir Mohammad Shojaee @ Electropeak
  Home

*/

#define RPWM 5
#define LPWM 6
#define REN 8
#define LEN 9


int pot;
int out1;
int out2;

void setup() {
  Serial.begin(9600);
  pinMode(RPWM,OUTPUT);
  pinMode(LPWM,OUTPUT);
  pinMode(LEN,OUTPUT);
  pinMode(REN,OUTPUT);
  digitalWrite(REN,HIGH);
  digitalWrite(LEN,HIGH);
  // analogWrite(LPWM, 25);
  // analogWrite(RPWM, 0);
  // delay(1000);
  // analogWrite(LPWM, 40);
  // analogWrite(RPWM, 0);
  // delay(1000);
  // analogWrite(LPWM, 50);
  // analogWrite(RPWM, 0);
  // delay(1000);
}
 
 
void loop() {
  
  // pot=analogRead(A0);
  // Serial.print(analogRead(A0));
  // Serial.print(" ");
  // Serial.println(map(pot,512,1023,0,255));
  // if(pot>512){
  //   out1=map(pot,512,1023,0,255);
  //   analogWrite(RPWM,out1);
  //   analogWrite(LPWM,0);
    
  // }
  
  // if(pot<512){
  //   out2=map(pot,512,0,0,255);
  //   analogWrite(LPWM,out2);
  //   analogWrite(RPWM,0);
  // }

  // for (int i = 5; i < 58; i++)
  // {
  //   Serial.print(i);
  //   Serial.println(" Straight move");
  //   analogWrite(LPWM, 0);
  //   analogWrite(RPWM, i);
  //   delay(300);
  // }
  // delay(3000);
  // for (int i = 57; i > 4; i--){
  //   Serial.print(i);
  //   Serial.println(" Straight move");
  //   analogWrite(LPWM, 0);
  //   analogWrite(RPWM, i);
  //   delay(300);
  // }
  // for (int i = 5; i < 58; i++){
  //   Serial.print(i);
  //   Serial.println(" Reverse");
  //   analogWrite(LPWM, i);
  //   analogWrite(RPWM, 0);
  //   delay(300);
  // }
  // delay(3000);
  // for (int i = 57; i > 4; i--){
  //   Serial.print(i);
  //   Serial.println(" Reverse");
  //   analogWrite(LPWM, i);
  //   analogWrite(RPWM, 0);
  //   delay(300);
  // }
  // delay(3000);
  analogWrite(LPWM, 230); //ток входа 1.6, ток коллектора 1.31 Ампера, Напряжение 7.4 Вольта
  analogWrite(RPWM, 0);
  delay(1000);
}
