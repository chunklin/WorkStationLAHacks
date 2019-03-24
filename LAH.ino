#include "DHT.h"
#include <math.h>

const int lightS = A1;
const int soundS = A2;
const int tempS = A0;
const int lockB = 4;
void setup()
{
    Serial.begin(115200);
  pinMode(tempS, INPUT);
  pinMode(lightS, INPUT);
  pinMode(soundS, INPUT);
  pinMode(lockB, INPUT);
}

void loop()
{
  while (true) {
  int t = analogRead(tempS);
  int lightVal = analogRead(lightS);
  int soundVal = analogRead(soundS);
  bool button = digitalRead(lockB);
  int lockV;
  if (button) lockV = 1;
  else  lockV = 0;
    // check if valid, if NaN (not a number) then something went wrong!
    //if (isnan(t) || isnan(h)) {
        //Serial.println("Failed to read from DHT");
        //return;
    //Serial.print("Humidity: ");
    //Serial.print(h);
    //Serial.print(" %\t");
    //Serial.print("Temperature: ");
  //Serial.print(" "+ lightVal + soundVal + "1" + lockV + t);
    //Serial.println(" *C");
     //2

    Serial.print(1); //1
    Serial.print(lockV); //1
    float t1 = 1023.0/t-1.0;
    t1=t1*100000;
    float temper = 1.0/(log(t1/100000)/4275+1/298.15)-273.15;
    Serial.print(temper); //4

    Serial.print(lightVal); //3
    
    Serial.print(soundVal); //3
 

    Serial.println(""); //5
    delay(1500);
}
}
