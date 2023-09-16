import cv2
import tensorflow as tf
import numpy as np

model = tf.keras.applications.MobileNetV2(weights='imagenet')

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

def predict_img(model, image):
    image = np.expand_dims(image, axis = 0)
    predictions = model.predict(image)
    return predictions

predictions = predict_img(model, image)

