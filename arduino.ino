#include "DHT.h"
#define DHTPIN 5
#define DHTTYPE DHT11
int h, t;
int body;
DHT dht(DHTPIN, DHTTYPE);
#include <Arduino.h>
#include <math.h>
#include <Wire.h>
float bpm = 0, so = 0;
#include "MAX30100.h"

MAX30100 *pulseOxymeter;

void setup()
{
    Wire.begin();
    Serial.begin(9600);

    dht.begin();
    // pulseOxymeter = new MAX30100( DEFAULT_OPERATING_MODE, DEFAULT_SAMPLING_RATE, DEFAULT_LED_PULSE_WIDTH, DEFAULT_IR_LED_CURRENT, true, true );
    pulseOxymeter = new MAX30100();
    pinMode(13, OUTPUT);
    pinMode(12, OUTPUT);
    pinMode(11, OUTPUT), pinMode(10, OUTPUT);
    pinMode(A2, INPUT);
    // pulseOxymeter->printRegisters();
}

void loop()
{
    // return;
    // You have to call update with frequency at least 37Hz. But the closer you call it to 100Hz the better, the filter will work.
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j <= 100; j++)
        {
            pulseoxymeter_t result = pulseOxymeter->update();
            if (result.pulseDetected == true)
            {
                bpm = result.heartBPM;
                so = result.SaO2;
                delay(10);
            }

            h = dht.readHumidity();
            t = dht.readTemperature();
            body = analogRead(A0);
            body = body * (5000 / 1023);
            body = body / 10;

            if (digitalRead(A2) == HIGH)
            {
                digitalWrite(11, HIGH);
                digitalWrite(13, LOW);
                digitalWrite(10, HIGH);
                if (bpm < 120 || bpm > 160)
                {
                    digitalWrite(12, HIGH);
                    digitalWrite(10, LOW);
                }
                else if (so < 85 || so > 93)
                {
                    digitalWrite(12, HIGH);
                    digitalWrite(10, LOW);
                }
                else if (h > 70 || h < 60)
                {
                    digitalWrite(12, HIGH);
                    digitalWrite(10, LOW);
                }
                else if (t > 22)
                {
                    digitalWrite(12, HIGH);
                    digitalWrite(10, LOW);
                }
                else if (body > 37.4 || body < 35)
                {
                    digitalWrite(12, HIGH);
                    digitalWrite(10, LOW);
                }
                else
                {
                    digitalWrite(12, LOW);
                }
            }
            else
            {
                digitalWrite(11, LOW);
                digitalWrite(10, HIGH);
                if (bpm < 80 || bpm > 140)
                {
                    digitalWrite(12, HIGH);
                    digitalWrite(13, LOW);
                    digitalWrite(10, LOW);
                }
                else if (so < 93 || so > 97)
                {
                    digitalWrite(12, HIGH);
                    digitalWrite(13, LOW);
                    digitalWrite(10, LOW);
                }
                else if (h > 60 || h < 40)
                {
                    digitalWrite(12, HIGH);
                    digitalWrite(13, LOW);
                    digitalWrite(10, LOW);
                }
                else if (t >= 23)
                {
                    digitalWrite(12, HIGH);
                    digitalWrite(13, LOW);
                    digitalWrite(10, LOW);
                }
                else if (body >= 38)
                {
                    digitalWrite(12, HIGH);
                    digitalWrite(13, LOW);
                    digitalWrite(10, LOW);
                }
                else if (t <= 20 || t > 22)
                {
                    digitalWrite(12, LOW);
                    digitalWrite(13, HIGH);
                    digitalWrite(10, LOW);
                }
                else if (body > 38 || body < 35)
                {
                    digitalWrite(12, LOW);
                    digitalWrite(13, HIGH);
                    digitalWrite(10, LOW);
                }
                else
                {
                    digitalWrite(12, LOW);
                }
            }
            delay(10);
        }
    }
    Serial.print(bpm);
    Serial.print(" ");
    Serial.print(so);
    Serial.print(" ");
    Serial.print(t);
    Serial.print(" ");
    Serial.print(h);
    Serial.print(" ");
    Serial.print(body);
    Serial.println(" ");
}
