# Usage: python ocr.py -i /home/images -o /home/tessoutput
# Writes Tesseract ensemble output to text files 
# You must have all the .traineddata files in your tessdata directory
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
ap.add_argument("-o", "--output_dir", help="Output directory for the files to be modified")
args = vars(ap.parse_args())

input_dir = args["input_dir"]
output_dir = args["output_dir"]

im_names = glob.glob(os.path.join(input_dir, '*.png'))

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file

langs = ['5x5_Dots_FT_500', 'dotOCRDData1'] 

for im_name in im_names:
    file_name = os.path.basename(im_name).split('.')[0]
    file_name = file_name.split()[0]
    print(file_name)
    print('\n')
    avg_confidences = []
    for i in range(len(langs)):
        data = pytesseract.image_to_data(Image.open(im_name), lang = langs[i], config='--psm 7', output_type=Output.DICT)
        debug = pytesseract.image_to_data(Image.open(im_name), lang = langs[i], config='--psm 7')
        print(debug)
        print('\n')
        text = data['text']
        confidences = []
        numChars = []

        for j in range(len(text)):
            if int(data['conf'][j]) > -1:
                confidences.append(int(data['conf'][j]))
                numChars.append(len(text[j]))

        if confidences != []:
            avg_confidences.append(np.average(confidences, weights=numChars))
            print(avg_confidences[i])
            print('\n')

    save_path = os.path.join(output_dir, file_name + ".txt")
    if avg_confidences != []:
        best = avg_confidences.index(max(avg_confidences))
        text = pytesseract.image_to_string(Image.open(im_name), lang = langs[best], config='--psm 7')
        f = open(save_path, "w")
        f.write(text)
        f.write('\n')
        print(text)
        print('\n')

    else:
        f = open(save_path, "x")
    

# show the output images
#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(0)
