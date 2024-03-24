#!/usr/bin/env python3

import pytesseract
import cv2

img_path = '/home/rene/github/OCR/temp/scans-for-OCR-tests/other-repos/A9T9/Free-OCR-API-CSharp/Test Images/eng-screenshot-verygood.jpg'

image = cv2.imread(img_path)


def remove_noise_and_smooth(img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
	kernel = np.ones((1, 1), np.uint8)
	opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN , kernel)
	closing = cv2.morphologyEx(opening , cv2.MORPH_CLOSE, kernel)
	ocr_image = image_smoothening(img)
	ocr_image = cv2.bitwise_or(img, closing)
	return ocr_image

# image = remove_noise_and_smooth(image)
# config = ("-l eng --oem 1 --psm 6")
text = pytesseract.image_to_string(image, config = ("-l eng --oem 1 --psm 6") )
print(text)
