import cv2
video=cv2.VideoCapture(0)
first_frame=None
while(True):
    c,frame=video.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (21, 21), 0)
    if(first_frame is None):
        first_frame=grey
        continue
    delta_frame=cv2.absdiff(first_frame,grey)
    thresh_frame=cv2.threshold(delta_frame,20,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)
    (k,dim)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cont in k:
        if (cv2.contourArea(cont)<1000):
            continue
        (x,y,w,h)=cv2.boundingRect(cont)
        cv2.rectangle(grey,(x,y),(x+w,y+h),(0,255,0),3)
    print(grey)
    print(delta_frame)
    cv2.imshow('Name',grey)
    cv2.imshow('Delta',delta_frame)
    cv2.imshow('Thresh',thresh_frame)
    k=cv2.waitKey(100)
    if(k==ord('q')):
        break
video.release()
cv2.destroyAllWindows()