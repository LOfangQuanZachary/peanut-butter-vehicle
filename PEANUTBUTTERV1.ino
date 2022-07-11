#include <Servo.h>
// depends on whether we use the servo or the stepper motor, preffereably servo as its easier
Servo frontWheel;
#define PWM1 3
#define PWM2 5
#define turnMotor 4
int powerA;
int powerB;
int turnDegree;
String toProcess;
int i;
int currentTime;
int timeElapsed;
int FPSrate;
int theDelaySync;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(PWM1, OUTPUT);
  pinMode(PWM2, OUTPUT);
  pinMode(turnMotor, OUTPUT);
  frontWheel.attach(turnMotor);
  initializationCode();
}

void loop() {
  // put your main code here, to run repeatedly:
  currentTime = millis();
  toProcess = serialInput();
  for(i = 0; i < toProcess.length(); i ++){
    if(i == 0 or i == 1 or i == 2){
      turnDegree = turnDegree + int(toProcess.charAt(i) * pow(10, 2 - i));
    }
    else if(i == 3 or i == 4 or i == 5 or i == 6){
      if(toProcess.charAt(i) == "-"){
        powerA = -1;
      }
      else{
        powerA = powerA + int(toProcess.charAt(i) * pow(10, 6 - i));
      }
    }
    else if(i == 9 or i == 10){
      if(toProcess.charAt(i) == "-"){
        powerB = -1;
      }
      else{
        powerB = powerB + int(toProcess.charAt(i) * pow(10, 10 - i));
      }
     }
    else{
        FPSrate = FPSrate + int(toProcess.charAt(i) * pow(10, 12 - i));
      }
  }
  turnControl(powerA, powerB, turnDegree);
  delay(1);
  timeElapsed = millis() - currentTime;
  theDelaySync = abs((1 / FPSrate * 1000) - timeElapsed);
  delay(theDelaySync);
}
void turnControl(int Astrength, int Bstrength, int turnAngle){
  analogWrite(PWM1, map(Astrength, -100, 100, -1024, 1024));
  analogWrite(PWM2, map(Bstrength, -100, 100, -1024, 1024));
  frontWheel.write(turnAngle);
}
String serialInput(){
  String data;
  if(Serial.available() > 0){
    data = Serial.readStringUntil("/n");
  }
  else{
    data = data;
    Serial.println("dataRequest");
  }
  if(data == "kill"){
    turnControl(0, 0, 0);
    while(true){
      delay(100);
    }
  }
  return data;
}
void initializationCode(){
  while(true){
    delay(100);
    if(serialInput == "Begin"){
      delay(100);
      Serial.println("StartingRun");
      break;
    }
  }
}
