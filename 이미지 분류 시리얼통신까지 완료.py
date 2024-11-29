import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
from tkinter import filedialog
import tkinter as tk
import serial
import time


py_serial = serial.Serial("COM3",9600)
time.sleep(1)

# 모델 로드
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# 웹캠에서 이미지를 캡처하는 함수
def capture_image():
    cam = cv2.VideoCapture(0)  # 웹캠 열기
    if not cam.isOpened():
        print("웹캠을 열 수 없습니다.")
        return None
    ret, frame = cam.read()
    if ret:
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))  # OpenCV의 BGR을 RGB로 변환 후 PIL 이미지로 변환
        cam.release()
        return img
    else:
        print("이미지 캡처 실패")
        cam.release()
        return None

# 파일 업로드(열기) 기능
def upload_image():
    root = tk.Tk()
    root.withdraw()  # Tkinter 창을 숨김
    file_path = filedialog.askopenfilename()  # 파일 선택 대화상자 표시
    if file_path:
        img = Image.open(file_path)
        return img
    else:
        print("파일을 선택하지 않았습니다.")
        return None

# 이미지 처리 및 분류
def process_and_classify_image(img):
    img = img.convert("RGB")  # RGBA에서 RGB로 변환
    img = img.resize((224, 224))  # 모델 입력 크기에 맞게 조정
    img_array = np.array(img) / 255.0  # 정규화
    img_array = np.expand_dims(img_array, axis=0)  # 배치 차원 추가

    predictions = model.predict(img_array)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)
    return decoded_predictions, img  # 분류 결과와 이미지를 반환

# 사용자에게 웹캠 또는 파일 업로드 선택
def main():
    choice = input("이미지 업로드 방식을 선택하세요 (1: 웹캠, 2: 파일 업로드): ")
    
    if choice == '1':
        print("웹캠을 사용하여 이미지를 캡처합니다.")
        img = capture_image()
    elif choice == '2':
        print("이미지 파일을 업로드하세요.")
        img = upload_image()
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")
        return

    if img:
        # 이미지 처리 및 분류
        result, captured_img = process_and_classify_image(img)

        # 캡처한 이미지를 출력
        captured_img.show()

        # 분류 결과 출력
        print(result)
        print("분류된 객체:", result[0][0][1])

    py_serial.write(result[0][0][1].encode("utf-8"))
    time.sleep(1)  # 대기 시간 늘리기

    if py_serial.readable():
            response = py_serial.readline().decode().strip()  # Read response from Arduino
            print(f"Arduino says: {response}")
    sum = py_serial.readline()

    sum = sum.decode()

    print(sum)

main()
