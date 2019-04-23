# Usage: python ocr_preprocess_image.py --image /home/tessinput/ex_37.png
# Does thresholding for dark images, where OTSU does not give high quality
# import the necessary packages
from PIL import Image
import argparse
import cv2
import os
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, gray = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cv2.imwrite(args["image"], gray)
os.system("convert -units PixelsPerInch " + args["image"] + " -density 300 -depth 8 -strip -background white -alpha off " + args["image"])
