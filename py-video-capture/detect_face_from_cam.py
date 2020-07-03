import cv2, time

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
# give 0 to detect camera
counter=0
while True:
    counter=counter+1
    check, frame = video.read()
    gray_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.5,
    minNeighbors=5)
    for x, y, w, h in faces:
        gray_img=cv2.rectangle(gray_img, (x,y), (x+w, y+h), (0, 255, 0), 3)
    # time.sleep(3)
    cv2.imshow("Capturing", gray_img)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

print(counter)
video.release()
cv2.destroyAllWindows()
