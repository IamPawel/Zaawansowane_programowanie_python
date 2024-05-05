import numpy as np
import cv2 as cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

img = cv2.imread("input.jpg")
#print(img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0) #czeka na klawisz
cv2.destroyAllWindows() #zamyka wszystkie okna  

#ta linijka odpowiada za wykrywanie ludzi na obrazie
boxes, weights = hog.detectMultiScale(gray, winStride=(32, 32) ) #winStride dzieli obraz na mniejsze fragmenty i sprawdza czy w nich znajduje sie czlowiek



#pętal rysująca prostokąty wokół wykrytych ludzi
boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
for (xA, yA, xB, yB) in boxes:
    # display the detected boxes in the colour picture
    cv2.rectangle(img, (xA, yA), (xB, yB),
                        (0, 255, 0), 2)
    
print(len(boxes))
cv2.imshow('img', img)
cv2.waitKey(0)

