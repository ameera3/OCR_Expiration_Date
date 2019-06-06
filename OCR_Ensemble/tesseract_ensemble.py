# Usage: python3 tesseract_ensemble.py -i /home/images -o /home/output
# import the necessary packages
from PIL import Image
import pytesseract
import io
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

im_names = sorted(glob.glob(os.path.join(input_dir, '*.png')))

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file

langs = ['5x5_Dots_FT_500', 'dotOCRDData1', 'Dotrice_FT_500', 'DotMatrix_FT_500',
         'DisplayDots_FT_500', 'LCDDot_FT_500', 'Orario_FT_500', 'Transit_FT_500'] 

for im_name in im_names:
    file_name = os.path.basename(im_name).split('.')[0]
    file_name = file_name.split()[0]
    print(file_name)
    print('\n')
    OCR_outputs = set()
    OCR_map = {}
    scores = []
    avg_confidences = []
    for i in range(len(langs)):
        data = pytesseract.image_to_data(Image.open(im_name), lang = langs[i], config='--psm 7', 
                output_type=Output.DICT)
        textString = pytesseract.image_to_string(Image.open(im_name), lang = langs[i], config='--psm 7')
        text = data['text']
        confidences = []
        numChars = []

        for j in range(len(text)):
            if int(data['conf'][j]) > -1:
                confidences.append(int(data['conf'][j]))
                numChars.append(len(text[j]))

        if confidences != []:
            avg_confidences.append(np.average(confidences, weights=numChars))
        else:
            avg_confidences.append(0)
        if textString not in OCR_outputs:
            OCR_outputs.add(textString)
            OCR_map[textString] = [i]
            scores.append(avg_confidences[i])
        else:
            scoreSum = avg_confidences[i]
            for j in OCR_map[textString]:
                scoreSum = scoreSum + avg_confidences[j]
            for j in OCR_map[textString]:
                scores[j] = scoreSum
            OCR_map[textString].append(i)
            scores.append(scoreSum)
    save_path = os.path.join(output_dir, file_name + ".txt")
    best = scores.index(max(scores))
    text = pytesseract.image_to_string(Image.open(im_name), lang = langs[best], config='--psm 7')
    count = 0
    if text != "":
        for c in text:
            if ( (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 65 and ord(c) <= 90) ):
                count = count + 1        
        if count/len(text) < 0.7:
            text = ""
    f = open(save_path, "w")
    f.write(text)
    f.write('\n')
    print(text)
    print('\n')
    print(best)
    print('\n')
    print(scores[best])
    print('\n')
    for key,val in OCR_map.items():
        print(key, "=>", val)
    print('\n')
