#include <Servo.h> // Servo 라이브러리를 추가
Servo servo;       // Servo 클래스로 servo 객체 생성
int value = 0;     // 각도를 조절할 변수 value

void setup() {
  servo.attach(7);   // attach 함수를 사용하여 핀 설정
  Serial.begin(9600); // 시리얼 모니터 사용 시작
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readString();  // 시리얼 데이터 읽기
    Serial.println("Data received: " + data);  // 수신된 데이터 출력

    // 받은 데이터에 따라 서보의 각도를 조정
    if (data.indexOf("ballpoint") >= 0) {
      value = 90;  // 'ballpoint'가 포함된 경우 90도 회전
    } else {
      value = -90; // 그 외의 경우 -90도 회전
    }

    servo.write(value); // value값의 각도로 회전
    delay(1000);        // 1초 대기
    //value = 0;          // 서보를 다시 0도로 설정
    servo.write(value);
  }
}
