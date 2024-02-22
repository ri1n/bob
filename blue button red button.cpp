// Buttons & LEDS
#define BLUE_LED_PIN     16
#define BLUE_BUTTON_PIN  17
#define RED_LED_PIN     18
#define RED_BUTTON_PIN  19

bool blueButtonLastState = 1;
bool redButtonLastState = 1;   // Last state of the button

int blueClicks = 0;
int redClicks = 0;
unsigned long redlastDebounceTime = 1;
unsigned long bluelastDebounceTime = 1;  // Last time the button was pressed
unsigned long debounceDelay = 100;    // Debounce time in milliseconds



void setup() {
  // Buttons & LEDS
  pinMode(BLUE_BUTTON_PIN, INPUT_PULLUP);  // Using internal pull-up resistor
  pinMode(BLUE_LED_PIN, OUTPUT);
    pinMode(RED_BUTTON_PIN, INPUT_PULLUP); 
  pinMode(RED_LED_PIN, OUTPUT);

  Serial.begin(115200);
}

void loop() {
// BLUE
  bool BlueButtonCurrentState = digitalRead(BLUE_BUTTON_PIN);
  if (BlueButtonCurrentState == 0 && blueButtonLastState == 1) {
    if ((millis() - bluelastDebounceTime) > debounceDelay) {   
    Serial.println("Blue Button has been pressed in the last 100Ms");
  // LED STUFF
    if (digitalRead(BLUE_LED_PIN) == 0) {
      digitalWrite(BLUE_LED_PIN, 1);
      }
    else if (digitalRead(BLUE_LED_PIN) == 1) {
      digitalWrite(BLUE_LED_PIN, 0);
      }
    // Serial.println(bluelastDebounceTime);
    // Serial.println(millis());
    blueClicks = blueClicks + 1;
    Serial.println(blueClicks);
    bluelastDebounceTime = millis();   
    }     
  }
  blueButtonLastState = BlueButtonCurrentState;


  bool RedButtonCurrentState = digitalRead(RED_BUTTON_PIN);
  if (RedButtonCurrentState == 0 && redButtonLastState == 1) {
    if ((millis() - redlastDebounceTime) > debounceDelay) {   
    Serial.println("Red Button has been pressed in the last 100Ms");
  // LED STUFF
    if (digitalRead(RED_LED_PIN) == 0) {
      digitalWrite(RED_LED_PIN, 1);
      }
    else if (digitalRead(RED_LED_PIN) == 1) {
      digitalWrite(RED_LED_PIN, 0);
      }
    // Serial.println(bluelastDebounceTime);
    // Serial.println(millis());
    redClicks = redClicks + 1;
    Serial.println(redClicks);
    redlastDebounceTime = millis();   
    }     
  }
  redButtonLastState = RedButtonCurrentState;
}