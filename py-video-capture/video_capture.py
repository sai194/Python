import cv2, time

video=cv2.VideoCapture(0)
# give 0 to detect camera
counter=0
while True:
    counter=counter+1
    check, frame = video.read()
    gray_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    cv2.imshow("Capturing", gray_img)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

print(counter)
video.release()
cv2.destroyAllWindows()
