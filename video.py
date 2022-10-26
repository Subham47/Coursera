import cv2,time

video = cv2.VideoCapture(0)
a=1
#check returns true or false if videois captured or not
#frame stores the numpy array of the first photo in the video
check, frame = video.read()
#print(check)
#print(frame)
cv2.imshow('Capturing', frame)
cv2.waitKey(0)

time.sleep(3)
video.release()
cv2.destroyAllWindows()