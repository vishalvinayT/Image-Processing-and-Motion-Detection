from datetime import datetime
import cv2
import pandas

first_frame=None
list=[None,None]
time_frame=[]
df=pandas.DataFrame(columns=['Start','Stop'])
vid=cv2.VideoCapture(0)
while(True):
    initial=0
    record,frame=vid.read()
    grey_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey_img=cv2.GaussianBlur(grey_img,(21,21),0)
    if(first_frame is None):
        first_frame=grey_img
        continue
    delta_frame=cv2.absdiff(first_frame,grey_img)
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)
    (bound,dim)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cont in bound:
        if(cv2.contourArea(cont)<10000):
            continue
        initial=1
        (x,y,w,h)=cv2.boundingRect(cont)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    list.append(initial)
    list=list[-2:]
    if(list[-1]==1 and list[-2]==0):
        time_frame.append(datetime.now())
    if(list[-1]==0 and list[-2]==1):
        time_frame.append(datetime.now())
    print(delta_frame)
    cv2.imshow('Diff',delta_frame)
    cv2.imshow('Thresh',thresh_frame)
    cv2.imshow('Main',frame)
    stp=cv2.waitKey(100)
    if(stp==ord('e')):
        break
print(time_frame)
df['Start']=[time_frame[i] for i in range(0,len(time_frame),2)]
df['Stop']=[time_frame[i] for i in range(1,len(time_frame),2)]
df.to_csv('Time_data.csv')
vid.release()
cv2.destroyAllWindows()

