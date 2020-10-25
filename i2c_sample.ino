#include <Arduino.h>
#include <Wire.h>
#define I2C_ADDRESS 0x21
#define LED_PIN 4
#define LIGHT_SENSOR 0
#define SWITCH_PIN 2

byte COM;

void receiveEvent(int DataNum){     
  COM = Wire.read();
  if(COM==0x01){
    digitalWrite(LED_PIN,HIGH);
  }else if(COM==0x02){
    digitalWrite(LED_PIN,LOW);
  }
}

void requestEvent() {
  byte d[2];
  int val;
  if(COM==0x01){
    val = analogRead(LIGHT_SENSOR);
    Serial.println(val);
    d[0] = val >> 8;
    d[1] = val;
    Wire.write(d,2);
  }else if (COM == 0x03){
    d[0] = digitalRead(SWITCH_PIN);
    Wire.write(d,1);
  }
}

void setup(){  
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  pinMode(SWITCH_PIN, INPUT);
  Wire.begin(I2C_ADDRESS);  
  Wire.onReceive(receiveEvent); 
  Wire.onRequest(requestEvent);                 
}


void loop() {

}
