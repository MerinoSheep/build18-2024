#include <MPU6050.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);

}
int i = 0;
void loop() {
  // put your main code here, to run repeatedly:
  // Change names to actual
  int sensor0 = analogRead(A0);
  int sensor1 = analogRead(A1);
  int sensor2 = analogRead(A2);
  int sensor3 = analogRead(A3);
  int sensor4 = analogRead(A4);

  char buffer[40];
  sprintf(buffer,"%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d",sensor0,sensor1,sensor2,sensor3,sensor4);
  Serial.println(buffer);
  i++;
  delay(500);
}