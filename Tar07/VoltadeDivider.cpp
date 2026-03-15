// Cargamos las librerias a utilizar
#include <Arduino.h>
#include <LiquidCrystal_I2C.h>


// Configuramos el LCD
LiquidCrystal_I2C lcd(0x27,16,2);


// Declaramos variables
int pinAnalog = A1;
int valorADC;
float voltaje;


void setup() {
  // Inicializamos la LCD
  lcd.init();
  lcd.clear();
  lcd.backlight();
}


void loop() {
  // Creamos una variable para almacenar el valor analogico
  int valor = analogRead(pinAnalog);


  // Transformamos a voltaje el valor leido
  float voltaje = valor * (5.0 / 1023.0);


  // Mostramos el voltaje en la LCD
  lcd.setCursor(0,0);
  lcd.print("Voltaje:");


  lcd.setCursor(0,1);
  lcd.print(voltaje);
  lcd.print(" V   ");


  // Repetimos lectura y calculo cada medio segundo
  delay(500);
}
