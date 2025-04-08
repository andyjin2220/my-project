import cv2
import mediapipe as mp

# MediaPipe pose 인식기 초기화
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Pose estimation 모델 로딩
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# 웹캠 열기
cap = cv2.VideoCapture(1)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("카메라를 찾을 수 없습니다.")
        break

    # 이미지 좌우반전 및 RGB 변환
    image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    # Pose 추정 실행
    results = pose.process(image)

    # 다시 BGR로 변환해서 시각화
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 관절 위치가 감지되었다면 스틱맨 그리기
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            image, 
            results.pose_landmarks, 
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=3),
            mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)
        )

    # 이미지 출력
    cv2.imshow('Stickman from Webcam', image)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC 키로 종료
        break

cap.release()
cv2.destroyAllWindows()
