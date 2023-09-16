import cv2

#opens a webcam or camera for image capture
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read() #read frame from camera
    cv2.imshow('Image Input', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#so far, this opens camera and quits if q is pressed
