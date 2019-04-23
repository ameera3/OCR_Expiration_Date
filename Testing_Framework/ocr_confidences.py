# Usage: python ocr_confidences.py -i /home/images
# Outputs the average confidence of each model in the ensemble on each image
# You must have all .traineddata files in your tessdata directory
# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import glob
import numpy as np
from pytesseract import Output

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_dir", help="Input directory for the files to be modified")
args = vars(ap.parse_args())

input_dir = args["input_dir"]

im_names = sorted(glob.glob(os.path.join(input_dir, '*.png')))

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file

langs = ['5x5_Dots_FT_500', 'Dot_Matrix_FT_500', 'dotOCRDData1'] 

for i in range(len(langs)):
    for im_name in im_names:
        file_name = os.path.basename(im_name).split('.')[0]
        file_name = file_name.split()[0]
        print(file_name + ': ', end='')
        data = pytesseract.image_to_data(Image.open(im_name), lang = langs[i], config='--psm 7', output_type=Output.DICT)
        text = data['text']
        confidences = []
        numChars = []

        for j in range(len(text)):
            if int(data['conf'][j]) > -1:
                confidences.append(int(data['conf'][j]))
                numChars.append(len(text[j]))

        if confidences != []:
            print(np.average(confidences, weights=numChars))
        else:
            print('0.00')

# show the output images
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(0)
