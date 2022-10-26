import cv2

#Creating a cascading classifier object
face_cascade = cv2.CascadeClassifier("C:\\Users\\subha\\docs\\Desktop\\Coursera\\Python\\work_place\\haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier("C:\\Users\\subha\\docs\\Desktop\\Coursera\\Python\\work_place\\haarcascade_eye.xml")

#Reading an image as it is
img = cv2.imread("C:\\Users\\subha\\Pictures\\basant\\face_detect.jpg")

#Converting it to gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Finding coordinates of faces in image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

resized = cv2.resize(img, (800,800))
cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
