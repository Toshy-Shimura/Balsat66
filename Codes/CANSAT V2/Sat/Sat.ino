//Librerias
#include <Wire.h>
#include <RH_NRF24.h>
#include <SPI.h>
#include "DHT.h"

//Pines
#define DHTPIN 2
#define DHTTYPE DHT22
#define CE_PIN 7
#define CSN_PIN 8
#define CHANNEL 123
#define PAYLOAD_SIZE 20

//Objetos
DHT dht(DHTPIN, DHTTYPE);
RH_NRF24 radio;

//Variables
int16_t ax, ay, az, gx, gy, gz;
float t, h;

void setup() {
  Wire.begin();
  Wire.beginTransmission(0x68);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);

  Serial.begin(9600);
  dht.begin();
  if (!radio.init()) {
    Serial.println("NRF24 initialization failed");
  }
  radio.setChannel(CHANNEL);
  radio.setRF(RH_NRF24::DataRate2Mbps, RH_NRF24::TransmitPower0dBm);
}

void loop() {
  Wire.beginTransmission(0x68);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(0x68, 14, true);

  ax = Wire.read() << 8 | Wire.read();
  ay = Wire.read() << 8 | Wire.read();
  az = Wire.read() << 8 | Wire.read();
  Wire.read();
  gx = Wire.read() << 8 | Wire.read();
  gy = Wire.read() << 8 | Wire.read();
  gz = Wire.read() << 8 | Wire.read();

  t = dht.readTemperature();
  h = dht.readHumidity();
  
  uint8_t data[PAYLOAD_SIZE];
  memcpy(data, &ax, 2);
  memcpy(data + 2, &ay, 2);
  memcpy(data + 4, &az, 2);
  memcpy(data + 6, &gx, 2);
  memcpy(data + 8, &gy, 2);
  memcpy(data + 10, &gz, 2);
  memcpy(data + 12, &t, 4);
  memcpy(data + 16, &h, 4);

  radio.send(data, PAYLOAD_SIZE);
  delay(100);
}
