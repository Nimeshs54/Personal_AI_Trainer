import numpy as np
import cv2
import time
import PoseEstimateModule as pm

cap = cv2.VideoCapture("Test.mp4")

detector = pm.PoseDetector()
count = 0
direction = 0
previous_time = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (720, 820))

    img = detector.getPose(img, draw=False)
    lmList = detector.getPosition(img, draw=False)

    if len(lmList) != 0:
        angle = detector.getAngle(img, 23, 25, 27)
        percentage = np.interp(angle, (130, 78), (0, 100))

        if percentage == 100:
            if direction == 0:
                count = count + 0.5
                direction = 1

        if percentage == 0:
            if direction == 1:
                count = count + 0.5
                direction = 0

        cv2.putText(img,f'Squats Count: {int(count)}', (30,750), cv2.FONT_HERSHEY_PLAIN, 4, (0,200,255), 5)

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time
        cv2.putText(img, f'fps: {int(fps)}', (30, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0, 0), 5)

    cv2.imshow("Video", img)
    cv2.waitKey(1)