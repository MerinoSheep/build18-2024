void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
int i = 0;
void loop() {
  // put your main code here, to run repeatedly:
  char buffer[40];
  sprintf(buffer,"%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d",i,i+1,i+2,i+3,i+4,i+5,i+6,i+7,i+8,i+9,i+10);
  Serial.println(buffer);
  i++;
  delay(400);
}
