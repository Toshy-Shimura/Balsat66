//Librerias
#include <RH_NRF24.h>
#include <SPI.h>
#include <LiquidCrystal_I2C.h>

#define CE_PIN 7
#define CSN_PIN 8
#define CHANNEL 123
#define PAYLOAD_SIZE 20


//Objetos
LiquidCrystal_I2C lcd(0x27,16,2);
RH_NRF24 radio;

int16_t ax, ay, az, gx, gy, gz, axms2, ayms2, azms2;
float t, h;
unsigned long lastTime = 0, sampleTime = 200;
int16_t girosc_ang_x, girosc_ang_y;
int16_t girosc_ang_x_prev, girosc_ang_y_prev;
long prev, dt;

void setup() {
  Serial.begin(9600);

  lcd.init();
  lcd.backlight();
  
  if (!radio.init()) {
    lcd.print("Error al iniciar");
  }
  radio.setChannel(CHANNEL);
  radio.setRF(RH_NRF24::DataRate2Mbps, RH_NRF24::TransmitPower0dBm);

  lcd.print("Base iniciada");
  lcd.setCursor(0, 1);
  lcd.print("Esperando datos...");
  
}

void loop() {
  if(millis()-lastTime>sampleTime)
  {
    lastTime = millis();
    uint8_t data[PAYLOAD_SIZE];
    uint8_t len = sizeof(data);

    if (radio.recv(data, &len)) {
      lcd.clear();
      lcd.setCursor(4, 0);
      lcd.print("BALSAT66");
      lcd.setCursor(3, 1);
      lcd.print("Conectado!");
    
      memcpy(&ax, data, 2);
      memcpy(&ay, data + 2, 2);
      memcpy(&az, data + 4, 2);
      memcpy(&gx, data + 6, 2);
      memcpy(&gy, data + 8, 2);
      memcpy(&gz, data + 10, 2);
      memcpy(&t, data + 12, 4);
      memcpy(&h, data + 16, 4);

      axms2 =  ax * (9.81/16384.0);
      ayms2 =  ay * (9.81/16384.0);
      azms2 =  az * (9.81/16384.0);

      float accel_ang_x=atan(ax/sqrt(pow(ay,2) + pow(az,2)))*(180.0/3.14);
      float accel_ang_y=atan(ay/sqrt(pow(ax,2) + pow(az,2)))*(180.0/3.14);
  
      Serial.println(axms2);
      Serial.println(ayms2);
      Serial.println(azms2);
      Serial.println(accel_ang_x);
      Serial.println(accel_ang_y);
      //Serial.println(gz);
      Serial.println(t);
      Serial.println(h);
    }
  }
}

float scaling(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
