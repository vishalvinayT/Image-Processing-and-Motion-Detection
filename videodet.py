import cv2,time
import finish
vid=cv2.VideoCapture('sample_video.mp4')
det=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
a=0
try:
    while(True):
        a=a+1
        check,frame=vid.read()
        print(check)
        print(frame)
        if(check==False):
            break
        else:
            frame=cv2.resize(frame,(int(frame.shape[0]/2),int(frame.shape[1]/5)))
            cv2.imshow('Pic',frame)
            k=cv2.waitKey(100)
            if(k==ord(('f'))):
                break
except cv2.error :
    print('Video Ended')
finally:
    print(a)
vid.release()
cv2.destroyAllWindows()