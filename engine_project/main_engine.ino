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

int value = 0; 
int lastButtonState = LOW; 
int currentButtonState;   
bool isPressed = false; 

void setup() {
  Serial.begin(9600);

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
}

void loop() {
  currentButtonState = digitalRead(button);

  if (currentButtonState == HIGH && lastButtonState == LOW && !isPressed) {
    isPressed = true; 
    value = (value == 0) ? 1 : 0; 
    Serial.println(value); 
  }

  if (currentButtonState == LOW) {
    isPressed = false;
  }

    lastButtonState = currentButtonState;
}
