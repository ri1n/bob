#include <LiquidCrystal_I2C.h>
#include "DHT.h"

#define DHTPIN 16     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);

// set the LCD number of columns and rows
int lcdColumns = 16;
int lcdRows = 2;
LiquidCrystal_I2C lcd(0x27, lcdColumns, lcdRows);  

unsigned long myTime;

void setup(){
  Serial.begin(115200);
  Serial.println(F("DHTxx test!"));
  // initialize LCD
  lcd.init();
  // turn on LCD backlight                      
  lcd.backlight();

  dht.begin();
}
float temploop(){
  // Wait a few seconds between measurements.
        
  // Read temperature as Celsius (the default)
     float t = dht.readTemperature();       

  return t;  
    }


// timer fiubauiebfibewri


void loop(){
   

  // float t = dht.readTemperature();  
  // set cursor to first column, first row
  lcd.setCursor(0, 0);
  // print message
  // lcd.print(t);
  lcd.print(temploop());
  lcd.print("C");
 
  // set cursor to first column, second row
  lcd.setCursor(0,1);
  lcd.print("Time: ");
  myTime = millis()/1000;

  lcd.print(myTime); // prints time since program started
   
  lcd.print(" Seconds");      // wait a second so as not to send massive amounts of data
  delay(2000); 
}
