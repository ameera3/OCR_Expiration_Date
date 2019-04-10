# Usage: python ocr_preprocess.py -i /home/images -o /home/images_processed
# Automatically does the image processing that Tesseract requires such as
# rescaling, binarisation, deskewing, removing alpha channel
# See https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality 

# import the necessary packages
from PIL import Image
import argparse
import cv2
import os
import glob
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_dir", help="Input directory for the files to be modified")
ap.add_argument("-o", "--output_dir", help="Output directory for the files to be modified")
args = vars(ap.parse_args())

input_dir = args["input_dir"]
output_dir = args["output_dir"]

im_names = glob.glob(os.path.join(input_dir, '*.png'))

for im_name in im_names:
    image = cv2.imread(im_name)
    file_name = os.path.basename(im_name).split('.')[0]
    file_name = file_name.split()[0]
    
    #convert image to grayscale, invert image for deskewing, threshold both gray and inverse
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverse = cv2.bitwise_not(gray)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    inverse = cv2.threshold(inverse, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
  
    # grab the (x, y) coordinates of all pixel values that
    # are greater than zero, then use these coordinates to
    # compute a rotated bounding box that contains all
    # coordinates
    coords = np.column_stack(np.where(inverse > 0))
    angle = cv2.minAreaRect(coords)[-1]

    # the `cv2.minAreaRect` function returns values in the
    # range [-90, 0); as the rectangle rotates clockwise the
    # returned angle trends to 0 -- in this special case we
    # need to add 90 degrees to the angle
    if angle < -45:
	angle = -(90 + angle)

    # otherwise, just take the inverse of the angle to make
    # it positive
    else:
	angle = -angle

    # rotate the image to deskew it
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(gray, M, (w, h),
	flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    # draw the correction angle on the image so we can validate it
    #cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
	#(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    save_path = os.path.join(output_dir, file_name + ".png")
    cv2.imwrite(save_path, rotated)
    os.system("convert -units PixelsPerInch " + save_path + " -density 300 -depth 8 -strip -background white -alpha off " + save_path)

