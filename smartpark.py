import cv2

img = cv2.imread("C:\\Users\\subha\\Pictures\\Free Image 1 -347-\\free_images\\Image514.jpg",1)
resized_img = cv2.resize(img, (int(img.shape[1]/4), int(img.shape[0]/8)))
print(img.shape)
print(resized_img.shape)
cv2.imshow("Image524.jpg", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(img.shape)