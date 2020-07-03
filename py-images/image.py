import cv2

img = cv2.imread("galaxy.jpg", 0)
# 0 is gray scale, 1 is rgb band
print(type(img))
print(img)
print(img.shape)
print(img.ndim)
resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(5000)
# 0 will keep window and closes on click
cv2.destroyAllWindows()
