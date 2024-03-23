#!/usr/bin/env python3

from PIL    import Image
from kraken import binarization

im = Image.open('/home/rene/github/temp/scans-for-OCR-tests/mine/tweet-177087971404902428.jpg')
bw_im = binarization.nlbin(im)
# type(bw_im) -> PIL.Image.Image
bw_im.save('tweet.png')

# -------------------------------------------------------------

from kraken import pageseg
seg = pageseg.segment(bw_im)
# type(seg) -> kraken.containers.Segmentation

print(seg.text_direction)

print(type(seg.lines)) # list
print(type(seg.lines[0])) kraken.containers.BBoxLine
print(len(seg.lines))


# -------------------------------------------------------------

from kraken.lib import models
