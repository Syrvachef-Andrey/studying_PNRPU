#include "OneWire.h"
#include "MAX31850.h"

#define svecha 2
#define RPWM_S 3
#define LPWM_S 4
#define REN_S 5
#define LEN_S 6
#define RPWM_N 7
#define LPWM_N 8
#define REN_N 9
#define LEN_N 10
#define button 11
#define ONE_WIRE_BUS 12
#define hallPin 13

int value = 0;
int lastButtonState = LOW;
int currentButtonState;
bool isPressed = false;
unsigned int hall = 0;

OneWire oneWire(ONE_WIRE_BUS);
MAX31850 sensor(&oneWire);

void setup() {
  Serial.begin(115200);

  pinModde(svecha, 1);
  pinMode(RPWM_S, 1);
  pinMode(LPWM_S, 1);
  pinMode(LEN_S, 1);
  pinMode(REN_S, 1);
  digitalWrite(REN_S, HIGH);
  digitalWrite(LEN_S, HIGH);
  pinMode(RPWM_N, 1);
  pinMode(LPWM_N, 1);
  pinMode(LEN_N, 1);
  pinMode(REN_N, 1);
  digitalWrite(REN_N, HIGH);
  digitalWrite(LEN_N, HIGH);
  pinMode(button, 0);
  pinMode(hallPin, 0);

  sensor.begin();
  sensor.requestTemperatures();
}

void loop() {
  currentButtonState = digitalRead(button);
  if (digitalRead(hallPin) > 0){
    hall++;
    }
  if (currentButtonState == 1 and lastButtonState == 0 and !isPressed) {
    isPressed = 1;
    value = (value == 0) ? 1 : 0;
    Serial.println(value);
  }

  if (currentButtonState == 0) {
    isPressed = 0;
  }
    lastButtonState = currentButtonState;
  if (currentButtonState == 1 and sensor.isCoversionComplete()){
    if (sensor.requestTemperatures() < 150 and (hall / 1000) < 10000){
    analogWrite(LPWM_S, 230);
    analogWrite(RPWM_S, 0);
    analogWrite(LPWM_N, 230);
    analogWrite(RPWM_N, 0);
    digitalWrite(svecha, 1);
    }
    else if(sensor.requestTemperatures() > 150 and (hall / 1000) > 10000){
    analogWrite(LPWM_S, 0);
    analogWrite(RPWM_S, 0);
    analogWrite(LPWM_N, 230);
    analogWrite(RPWM_N, 0);
    digitalWrite(svecha, 1);
    }
    else if(sensor.requestTemperatures() > 150 and (hall / 1000) > 30000){
    analogWrite(LPWM_S, 180);
    analogWrite(RPWM_S, 0);
    analogWrite(LPWM_N, 0);
    analogWrite(RPWM_N, 0);
    digitalWrite(svecha, 0);
    }
  }
}
