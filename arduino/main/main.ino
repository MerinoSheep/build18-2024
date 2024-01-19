#include <MPU6050.h>
#include<Wire.h>

MPU6050 mpu;
int16_t ax, ay, az;
int16_t gx, gy, gz;
const int MPU_ADDR=0x68;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  
  // mpu.initialize();
  Wire.begin();
  mpu.initialize();
  mpu.setFullScaleAccelRange(MPU6050_ACCEL_FS_4);
  mpu.setFullScaleGyroRange(MPU6050_GYRO_FS_2000);
}
// AX: -156, AY: -228, AZ: 16496, GX: -3952, GY: 48,GZ: -16
// AX: -288, AY: 64, AZ: 16268, GX: -3984, GY: -14,GZ: -13
// AX: -68, AY: 72, AZ: 16532, GX: -4016, GY: -14,GZ: -22
// AX: -20, AY: 48, AZ: 16300, GX: -4016, GY: -35,GZ: 20
// AX: -68, AY: -40, AZ: 16632, GX: -4000, GY: -5,GZ: -2
// AX: -40, AY: 60, AZ: 16368, GX: -4016, GY: 22,GZ: 31
// AX: 20, AY: -28, AZ: 16480, GX: -4016, GY: -42,GZ: -22
// AX: -92, AY: 12, AZ: 16536, GX: -3984, GY: 10,GZ: -37
// AX: -116, AY: 12, AZ: 16496, GX: -4000, GY: 8,GZ: -10
// AX: -80, AY: -16, AZ: 16376, GX: -4000, GY: -25,GZ: 5
void loop() {
  // put your main code here, to run repeatedly:
  // Change names to actual
  int sensor0 = analogRead(A0);
  int sensor1 = analogRead(A1);
  int sensor2 = analogRead(A2);
  int sensor3 = analogRead(A3);
  Wire.beginTransmission(MPU_ADDR);
  mpu.getMotion6(&ax,&ay,&az,&gx,&gy,&gz);

  char buffer[40];
  sprintf(buffer,"%d,%d,%d,%d,%d,%d,%d,%d,%d,%d", ax, ay, az, gx, gy, gz, sensor0,sensor1,sensor2,sensor3);
  // sprintf(buffer,"%d,%d,%d,%d,%d,%d",ax,ay,az,gx,gy,gz);
  Serial.println(buffer);
  delay(10);
}