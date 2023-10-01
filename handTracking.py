import cv2
import cvlearn.HandTrackingModule as htm
import cvlearn.FingerCounter as counter
cap=cv2.VideoCapture(0)
detector=htm.handDetector()
fingercounter=counter.FingerCounter()
while True:
    ret, frame=cap.read()
    detector.findHands(frame)
    lmList, bbox=detector.findPosition(frame)
    if lmList!=0:
        fingercounter.drawCountedFingers(frame,lmList,bbox)
    cv2.imshow("result",frame)
    cv2.waitKey(1)

