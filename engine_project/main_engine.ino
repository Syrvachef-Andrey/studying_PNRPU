#include "OneWire.h"
#include "MAX31850.h"

#define holl 0
#define r_en_starter 9
#define l_en_starter 8
#define r_pwm_starter 11
#define l_pwm_starter 10
#define r_en_nasos 4
#define l_en_nasos 7
#define r_pwm_nasos 5
#define l_pwm_nasos 6
#define svecha 13
#define one_wire_bus_termopara 2
#define klapan_the_first 3
#define klapan_the_second 12

OneWire oneWire(one_wire_bus_termopara);
MAX31850 sensor(&oneWire);

int signal_from_holl;

void setup(void)
{
  Serial.begin(115200);
  Serial.println();
  Serial.println(__FILE__);
  Serial.print("MAX31850_LIB_VERSION: ");
  Serial.println(MAX31850_LIB_VERSION);
  pinMode(holl, INPUT);
  pinMode(r_pwm_starter, OUTPUT);
  pinMode(l_pwm_starter, OUTPUT);
  pinMode(l_en_starter, OUTPUT);
  pinMode(r_en_starter, OUTPUT);
  pinMode(r_pwm_nasos, OUTPUT);
  pinMode(l_pwm_nasos, OUTPUT);
  pinMode(l_en_nasos, OUTPUT);
  pinMode(r_en_nasos, OUTPUT);
  pinMode(klapan_the_first, OUTPUT);
  pinMode(klapan_the_second, OUTPUT);
  pinMode(svecha, OUTPUT);
  digitalWrite(r_en_starter,HIGH);
  digitalWrite(l_en_starter,HIGH);
  digitalWrite(r_en_nasos,HIGH);
  digitalWrite(l_en_nasos,HIGH);
  sensor.begin();
  sensor.requestTemperatures();
}


void loop(void)
{
  if (sensor.isConversionComplete())
  {
    sensor.read();
    Serial.print("TC:\t");
    Serial.println(sensor.getTempTC());
    Serial.print("INTERN:\t");
    Serial.println(sensor.getTempInternal());
    Serial.println();
    sensor.requestTemperatures();
  }
//  analogWrite(l_pwm_starter, 230);
//  analogWrite(r_pwm_starter, 0);
//  delay(3000);
//  analogWrite(l_pwm_starter, 0);
//  analogWrite(r_pwm_starter, 0);  // стартер
//  delay(3000);
//  digitalWrite(klapan_the_first, 1);
//  digitalWrite(klapan_the_second, 1);
//  delay(3000);
//  digitalWrite(klapan_the_first, 0);
//  digitalWrite(klapan_the_second, 0);
//  delay(3000); // клапана
//  digitalWrite(svecha, 1); // свеча
//  analogWrite(l_pwm_nasos, 230);
//  analogWrite(r_pwm_nasos, 0);
//  delay(3000);
//  analogWrite(l_pwm_nasos, 0);
//  analogWrite(r_pwm_nasos, 0);
//  delay(3000); // насос

}