import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


def adjusted_detect_face(img):
    face_img = img.copy()
    face_rect = face_cascade.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
        
    return face_img


url = 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Shraddha_Kapoor_promoting_Street_Dancer_3D.jpg'
resp = urllib.request.urlopen(url)
image_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)


img_copy1 = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()


plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

detected = adjusted_detect_face(img)
plt.imshow(cv2.cvtColor(detected, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()







