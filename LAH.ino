#include "DHT.h"

DHT dht(A0, DHT11);
const int lightS = A1;
const int soundS = A2;
const int lockB = 4;
void setup()
{
    Serial.begin(115200);
    dht.begin();
  pinMode(lightS, INPUT);
  pinMode(soundS, INPUT);
  pinMode(lockB, INPUT);
}

void loop()
{
    float h = dht.readHumidity();
    float t = dht.readTemperature();
  int lightVal = analogRead(lightS);
  int soundVal = analogRead(soundS);
  bool button = digitalRead(lockB);
  int lockV;
  if (button) lockV = 1;
  else  lockV = 0;
    // check if valid, if NaN (not a number) then something went wrong!
    if (isnan(t) || isnan(h)) {
        //Serial.println("Failed to read from DHT");
        return;
}
  
    //Serial.print("Humidity: ");
    //Serial.print(h);
    //Serial.print(" %\t");
    //Serial.print("Temperature: ");
  //Serial.print(" "+ lightVal + soundVal + "1" + lockV + t);
    //Serial.println(" *C");
    Serial.print(" ");
    Serial.print(lightVal);
    Serial.print(soundVal);
    Serial.print(1);
    Serial.print(lockV);
    Serial.print(t);
    delay(2000);
}
