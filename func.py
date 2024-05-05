import numpy as np
import cv2 as cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def get_count_people(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (640, 480))

    boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8)) #winStride dzieli obraz na mniejsze fragmenty i sprawdza czy w nich znajduje sie czlowiek
    return len(boxes)

print(get_count_people(cv2.imread("input.jpg")))