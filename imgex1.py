import cv2
a=cv2.imread("D:\\udemyprojects\\Image processing\\sample_images\\galaxy.jpg",0)
print(a.shape)
new_size=cv2.resize(a,(int(a.shape[0]/2),int(a.shape[1]/2)))
cv2.imshow('Galxy',new_size)
cv2.waitKey(3000)
cv2.destroyAllWindows()

