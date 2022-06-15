import cv2
import os,glob
for file in glob.glob("D:\\udemyprojects\\Image processing\\sample_images\\*.jpg"):
    a = cv2.imread(file, 0)
    new_file = cv2.resize(a, (100, 100))
    cv2.imshow('Photo', new_file)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    cv2.imwrite('resized_' + file, new_file)
