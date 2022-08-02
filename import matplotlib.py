from msvcrt import getch
from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret,frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break