#include <MPU6050.h>
#include<Wire.h>
#include "letter.h"
#include "Arduino_LED_Matrix.h"
#include "arduino_secrets.h"
ArduinoLEDMatrix matrix;
MPU6050 mpu;
int16_t ax, ay, az;
int16_t gx, gy, gz;
int incomingByte = 0; // for incoming serial data
const int MPU_ADDR=0x68;
char ssid[] = SECRET_SSID;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);

  mpu.initialize();
  Wire.begin();
  mpu.initialize();
  mpu.setFullScaleAccelRange(MPU6050_ACCEL_FS_4);
  mpu.setFullScaleGyroRange(MPU6050_GYRO_FS_2000);
  matrix.begin();
  // WiFi.begin(ssid);
}
void loop() {
  int sensor0 = analogRead(A0);
  int sensor1 = analogRead(A1);
  int sensor2 = analogRead(A2);
  int sensor3 = analogRead(A3);
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read() - 'A';
    matrix.loadFrame(letters[incomingByte]);
  }
  Wire.beginTransmission(MPU_ADDR);
  mpu.getMotion6(&ax,&ay,&az,&gx,&gy,&gz);
  
  char buffer[40];
  sprintf(buffer,"%d,%d,%d,%d,%d,%d,%d,%d,%d,%d", ax, ay, az, gx, gy, gz, sensor0,sensor1,sensor2,sensor3);
  Serial.println(buffer);
  delay(10);
}

