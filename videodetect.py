import cv2,pandas
from datetime import datetime
video=cv2.VideoCapture(0)
df=pandas.DataFrame(columns=['Start','End'])
first_frame=None
status_lst=[None,None]
time=[]
while(True):
    status=0
    c,frame=video.read()   
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (21, 21), 0)
    if(first_frame is None):
        first_frame=grey
        continue
    delta_frame=cv2.absdiff(first_frame,grey)
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)
    (k,dim)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cont in k:
        if (cv2.contourArea(cont)<10000):
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(cont)
        cv2.rectangle(grey,(x,y),(x+w,y+h),(0,255,0),3)
    status_lst.append(status)
    if(status_lst[-1]==1 and status_lst[-2]==0):
        time.append(datetime.now())
    if(status_lst[-1]==0 and status_lst[-2]==1):
        time.append(datetime.now())
    print(grey)
    print(delta_frame)
    cv2.imshow('Name',grey)
    cv2.imshow('Delta',delta_frame)
    cv2.imshow('Thresh',thresh_frame)
    k=cv2.waitKey(100)
    if(k==ord('q')):
        if(status==1):
            time.append(datetime.now())
        break
print(time)
df['Start']=[time[i] for i in range(0,len(time),2)]
df['End']=[time[i] for i in range(1,len(time),2)]
df.to_csv('Times.csv')
video.release()
cv2.destroyAllWindows()
