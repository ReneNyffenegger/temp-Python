#!/usr/bin/env python3


#
#   After capturing images, create movie like so:
#      ffmpeg -framerate 15 -pattern_type glob -i '*.jpg' -c:v libx264 -pix_fmt yuv420p out-3.mp4
#

import cv2
import time

cam = cv2.VideoCapture(0)

cv2.namedWindow('frame-out')
cnt = 0

while True:

      ret, frame = cam.read()  #read frame
      if not ret:
         break

      cv2.imshow('frame-out', frame)

      keyPressed = cv2.waitKey(1)

      if   keyPressed % 256 == 27:
         # ESC pressed: exit loop

           break

t = time.time()
for cnt in range(10000):

      ret, frame = cam.read()

      if not ret:
         break
cv2.imshow('frame-out', frame)
      img_name = f'timelapse-{cnt:04d}.jpg'
      cv2.imwrite(img_name, frame)
      print(f'{img_name} written')

      time.sleep(1)


cam.release()
cv2.destroyAllWindows()
