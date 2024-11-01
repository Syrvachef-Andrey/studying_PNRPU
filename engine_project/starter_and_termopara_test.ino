#include "OneWire.h"
#include "MAX31850.h"

#define RPWM 5
#define LPWM 6
#define REN 8
#define LEN 9
#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);
MAX31850 sensor(&oneWire);

int pot;
int out1;
int out2;

void setup() {
  Serial.begin(115200);
  Serial.println();
  Serial.println(__FILE__);
  Serial.print("MAX31850_LIB_VERSION: ");
  Serial.println(MAX31850_LIB_VERSION);
  sensor.begin();
  sensor.requestTemperatures();
  pinMode(RPWM, OUTPUT);
  pinMode(LPWM, OUTPUT);
  pinMode(LEN, OUTPUT);
  pinMode(REN, OUTPUT);
  digitalWrite(REN, 1);
  digitalWrite(LEN, 1);
  delay(2000);
  while (1){
        analogWrite(LPWM, 255);
        analogWrite(RPWM, 0);
        if (sensor.isConversionComplete())
      {
        sensor.read();
        Serial.print("TC:\t");
        Serial.println(sensor.getTempTC());
        Serial.print("INTERN:\t");
        Serial.println(sensor.getTempInternal());
        Serial.println();
        sensor.requestTemperatures();
        if (sensor.getTempTC() > 40){
          break;
        }
      }
    }
    Serial.println("FINAL");
    analogWrite(LPWM, 255 / 2);
    analogWrite(RPWM, 0);
    delay(1000);
    analogWrite(LPWM, 0);
    analogWrite(RPWM, 0);
}

void loop() {
    
}
