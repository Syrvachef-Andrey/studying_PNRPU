// #include "OneWire.h"
// #include "MAX31850.h"


// #define ONE_WIRE_BUS    2


// OneWire oneWire(ONE_WIRE_BUS);
// MAX31850 sensor(&oneWire);


// DeviceAddress da;


// void setup()
// {
//   Serial.begin(115200);
//   Serial.println(__FILE__);
//   Serial.print("MAX31850_LIB_VERSION: ");
//   Serial.println(MAX31850_LIB_VERSION);

//   Serial.print("\ngetAddress: ");
//   Serial.println(sensor.getAddress(da));
  
//   sensor.begin();

//   Serial.print("\ngetAddress: ");
//   Serial.println(sensor.getAddress(da));

//   if (!sensor.getAddress(da))
//   {
//     Serial.println("No address found!");
//     return;
//   }

//   Serial.print("Address: ");
//   for (uint8_t i = 0; i < 8; i++)
//   {
//     if (da[i] < 0x10) Serial.print('0');
//     Serial.print(da[i], HEX);
//   }
//   Serial.println();
// }


// void loop()
// {
// }

#include "OneWire.h"
#include "MAX31850.h"


#define ONE_WIRE_BUS    2


OneWire oneWire(ONE_WIRE_BUS);
MAX31850 sensor(&oneWire);


void setup(void)
{
  Serial.begin(115200);
  Serial.println();
  Serial.println(__FILE__);
  Serial.print("MAX31850_LIB_VERSION: ");
  Serial.println(MAX31850_LIB_VERSION);

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
}