// Establecemos las librerias
#include <Arduino.h>
#include <DHT.h>
#include <LiquidCrystal_I2C.h>


// Definimos variables
#define DHTPIN 2
#define DHTTYPE DHT11


// Configuramos hardware
DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(0x27, 16, 2);
// S del DHT va a pin2_UNO
// SDA (data) de I2C va a SDA_UNO
// SCL (clock) de I2C va a SCL_UNO


void setup() {
 // Proceso de inicialización y limpiado del LCD
 lcd.init();
 lcd.clear();
 lcd.backlight();


 // Mostramos el texto en 2,0
 lcd.setCursor(2, 0);
 lcd.print("Aprender es");


 // Mostramos el siguiente texto en 6,1
 lcd.setCursor(6,1);
 lcd.print("muy chido");
 dht.begin();
}
void loop() {
 delay(2000); // Esperamos 2 seg


 // Declaramos variables donde almacenamos las lecturas de humedad y temperatura
 float h = dht.readHumidity();
 float t = dht.readTemperature();


 // Condicionamos para cuando las lecturas son vacias/fallidas
 if (isnan(h) || isnan(t)) {
  lcd.setCursor(0,0);
  lcd.print("Falló lectura");
  lcd.setCursor(0,1);
  lcd.print("del sensor DHT!");
  return;
 }

 // Mostramos en 0,0 la humedad
 lcd.setCursor(0,0);
 lcd.print("Hum: ");
 lcd.print(h);
 lcd.print("%   ");


 // Mostramos en 0,1 la temperatura
 lcd.setCursor(0,1);
 lcd.print("Temp: ");
 lcd.print(t);
 lcd.print((char)223); //char de grados Celsius y mas -> https://docs.wokwi.com/parts/wokwi-lcd1602
 lcd.print("C   ");
}
