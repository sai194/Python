import cv2, time

first_frame=None
video=cv2.VideoCapture(0)
# give 0 to detect camera
counter=0
while True:
    counter=counter+1
    check, frame = video.read()
    status=0
    gray_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_img=cv2.GaussianBlur(gray_img, (21,21), 0)
    if first_frame is None:
        first_frame=gray_img
        continue
    delta_frame=cv2.absdiff(first_frame, gray_img)
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 70000:
            continue
        status=1
        (x, y, w, h)=cv2.boundingRect(contour)
        print(x,y,w,h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
    # time.sleep(3)
    cv2.imshow("Gray Frame", gray_img)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    print(status)

print(counter)
video.release()
cv2.destroyAllWindows()
