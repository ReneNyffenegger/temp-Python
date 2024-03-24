#!/usr/bin/env python3

import pytesseract
import cv2

img_path = '/home/rene/github/OCR/temp/scans-for-OCR-tests/other-repos/A9T9/Free-OCR-API-CSharp/Test Images/eng-screenshot-verygood.jpg'

image = cv2.imread(img_path)

text = pytesseract.image_to_string(image, config = ("-l eng --oem 1 --psm 6") )
print(text)
