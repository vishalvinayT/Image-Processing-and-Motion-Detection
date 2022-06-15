import cv2,numpy
cas=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('news.jpg')
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dtec=cas.detectMultiScale(grey_img,scaleFactor=1.2,minNeighbors=7)
print(dtec,type(dtec))
for x,y,w,h in dtec:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)
resize=cv2.resize(img,((int(img.shape[0]/3)),(int(img.shape[1]/3))))
cv2.imshow('Pic',resize)
cv2.waitKey(0)
cv2.destroyAllWindows()