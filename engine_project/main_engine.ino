#include "OneWire.h"
#include "MAX31850.h"

// --- ПИНЫ ---
#define holl 3
#define klapan_the_first A0
#define klapan_the_second 12

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

OneWire oneWire(one_wire_bus_termopara);
MAX31850 sensor(&oneWire);

String inputCommand = "";

void setup() {
  Serial.begin(115200);
  Serial.println("Система управления ГТД инициализирована.");
  Serial.println("Доступны команды с параметрами (0-255), например: 'стартер 150' или 'насос 90'");
  Serial.println("Базовые команды: 'свеча', 'запуск', 'стоп'");

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

  digitalWrite(r_en_starter, HIGH);
  digitalWrite(l_en_starter, HIGH);
  digitalWrite(r_en_nasos, HIGH);
  digitalWrite(l_en_nasos, HIGH);

  sensor.begin();
  sensor.requestTemperatures();
}

void loop() {
  // Чтение температуры
  if (sensor.isConversionComplete()) {
    sensor.read();
    sensor.requestTemperatures();
  }

  // Обработка команд из Serial Monitor
  if (Serial.available() > 0) {
    inputCommand = Serial.readStringUntil('\n');
    inputCommand.trim();

    if (inputCommand.length() > 0) {
      parseAndExecute(inputCommand);
    }
  }
}

// ==========================================
// ФУНКЦИИ ПАРСИНГА И ЛОГИКИ
// ==========================================

// Новая функция для разделения текста и цифр
void parseAndExecute(String input) {
  String cmd = "";
  int value = -1; // -1 означает, что числовой параметр не передан

  // Ищем индекс пробела в строке
  int spaceIndex = input.indexOf(' ');

  if (spaceIndex != -1) {
    // Если пробел найден, делим строку на команду и значение
    cmd = input.substring(0, spaceIndex);
    String valStr = input.substring(spaceIndex + 1);
    valStr.trim();

    // Превращаем текст в число, если там действительно цифры
    if (valStr.length() > 0) {
      value = valStr.toInt();
    }
  } else {
    // Если пробела нет, вся строка — это команда
    cmd = input;
  }

  cmd.trim();
  cmd.toLowerCase(); // Защита от разного регистра (СТАРТЕР -> стартер)

  // Исполнение команд
  if (cmd == "стартер") {
    // Если значение не ввели или оно некорректно, ставим дефолт 150
    int targetSpeed = (value >= 0 && value <= 255) ? value : 150;
    Serial.print("Команда: Стартер -> Скорость: ");
    Serial.println(targetSpeed);
    setStarterState(true, targetSpeed);
  }
  else if (cmd == "насос") {
    // Если значение не ввели или оно некорректно, ставим дефолт 100
    int targetSpeed = (value >= 0 && value <= 255) ? value : 100;
    Serial.print("Команда: Насос -> Скорость: ");
    Serial.println(targetSpeed);
    setPumpState(true, targetSpeed);
  }
  else if (cmd == "свеча") {
    Serial.println("Команда: Накал свечи...");
    setGlowPlugState(true);
  }
  else if (cmd == "запуск") {
    Serial.println("Команда: ЗАПУСК ПОСЛЕДОВАТЕЛЬНОСТИ!");
    startupSequence();
  }
  else if (cmd == "стоп") {
    Serial.println("Команда: ЭКСТРЕННАЯ ОСТАНОВКА!");
    emergencyStop();
  }
  else {
    Serial.println("Неизвестная команда. Пример: 'стартер 150', 'насос 80', 'стоп'");
  }
}

void setStarterState(bool state, int speed) {
  if (state) {
    analogWrite(r_pwm_starter, speed);
    analogWrite(l_pwm_starter, 0);
  } else {
    analogWrite(r_pwm_starter, 0);
    analogWrite(l_pwm_starter, 0);
  }
}

void setPumpState(bool state, int speed) {
  if (state) {
    analogWrite(r_pwm_nasos, speed);
    analogWrite(l_pwm_nasos, 0);
  } else {
    analogWrite(r_pwm_nasos, 0);
    analogWrite(l_pwm_nasos, 0);
  }
}

void setGlowPlugState(bool state) {
  digitalWrite(svecha, state ? HIGH : LOW);
}

void startupSequence() {
  Serial.println(">>> 1. Раскрутка стартера (скорость 150)...");
  setStarterState(true, 150);
  delay(2000);

  Serial.println(">>> 2. Подача напряжения на свечу...");
  setGlowPlugState(true);
  delay(3000);

  Serial.println(">>> 3. Подача топлива (скорость 100)...");
  setPumpState(true, 100);

  Serial.println(">>> ОЖИДАНИЕ ВОСПЛАМЕНЕНИЯ.");
}

void emergencyStop() {
  setStarterState(false, 0);
  setPumpState(false, 0);
  setGlowPlugState(false);
  Serial.println("Все системы принудительно отключены.");
}