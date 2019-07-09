# Expiration_Date

Copyright 2019, by the California Institute of Technology. ALL RIGHTS RESERVED. United States Government Sponsorship acknowledged. Any commercial use must be negotiated with the Office of Technology Transfer at the California Institute of Technology.
     
This software may be subject to U.S. export control laws. By accepting this software, the user agrees to comply with all applicable U.S. export laws and regulations. User has the responsibility to obtain export licenses, or other export authority as may be required before exporting such information to foreign countries or providing access to foreign persons.

## Introduction

For a detailed introduction, see the [Slides](../master/OCRDotMatrix.pdf).

Our team designs software for the Department of Homeland Security’s Next Generation First Responder program. Imagine that you have had a heart attack. The paramedics that treat you need to know which medications you are currently taking, as this will influence which procedures or therapies they will administer. However, you are incapacitated and cannot tell them. 

The paramedic looks in your medicine cabinet and finds a vial of medication. Correctly recording and quickly communicating your medication to everyone on the medical team is crucial.  Our team is developing optical character recognition (OCR) software that can correctly read vital information from a photo of a medicine bottle, such as the medication’s name, the dose, the lot number and the expiration date.  

Our experiments show that lot numbers and expiration dates are particularly difficult for off-the-shelf OCR engines, such as Tesseract, to read because they are usually written in a dot-matrix font that varies widely from product to product. For example, Tesseract and the Google Text Detection API achieve a 55% and 60% character accuracy, respectively, on dot matrix fonts. 

To improve the character accuracy and to mitigate the wide variation in dot matrix fonts, we have developed an image processing pipeline as well as a novel way to ensemble OCR outputs. Our current ensemble consists of the Google Document Text Detection API and eight models trained using Tesseract's LSTM neural network. We achieve 87% character accuracy with 41 out of 75 test samples achieving perfect 100% character accuracy. Moreover, for 54 of the 75 test examples, the intended information can be extracted without error from the ensemble's outputs. Our ensemble's character accuracy is an 8% improvement on that of the Google Document Text Detection API.

The code on Github has five major functions:

1. Creating and supporting the Google+Tesseract ensemble
2. Reporting Results
3. Image-processing pipeline
4. Testing framework
5. Custom dot-matrix font dataset used to create the most successful model in the Tesseract ensemble

Below, all the programs on Github are organized by their function:

## Creating and supporting the Google+Tesseract ensemble

User Manual -- Start here if you intend to run the programs in this repository. Provides suggestions for programs to install before running the programs in this repository. Command line instructions to run each program are found at the top of each program in the repository.

Traineddata Files -- There are eight custom dot matrix traineddata files. These .traineddata files were created by fine-tuning Tesseract’s LSTM neural network on the respective dot matrix fonts.  These are the eight models used in the current Tesseract ensemble.

gplust_ensemble.py -- This program produces the Google+Tesseract ensemble output from the Google Document Text Detection API and our eight .traineddata files.

tesseract_ensemble.py -- This program produces the Tesseract ensemble output from the eight .traineddata files.

dot_training_text.txt -- The training data that is used to fine-tune Tesseract's neural network to the eight dot matrix fonts.

Prepare_Training_Text.ipynb -- Used to create dot_training_text.txt

## Reporting Results

**The Good** -- Illustrates the 54 out of 75 test examples for which it is possible to extract the intended information without error from the ensemble's output.

**The Mostly OK** -- Illustrates the 14 out of 75 test examples for which it is possible to extract the intended information with minor errors from the ensemble's output.

**The Bad and The Ugly** -- Illustrates the 7 out of 75 test examples for which it is not possible to extract the intended information from the ensemble's output.

**Adding Google Document Text Detection to Ensemble** -- The first column gives the results for Google Document Text Detection’s API with no image processing. The second column gives the results for Google’s Document Text Detection API with my image processing. Observe that my image processing increases the average character accuracy by over 6%. 

The third column gives the results of my Google + Tesseract ensemble with no image processing. Comparing with the second column, we see that the Google + Tesseract ensemble's character accuracy is a 4% improvement on that of the Google Document Text Detection API on the raw images. 

The last column gives the results for my Google + Tesseract ensemble with my image processing. Comparing with the third column, we see that my image processing increases the average accuracy of the Google + Tesseract ensemble by over 10%. Comparing with the second column, we see that the Google + Tesseract character accuracy ensemble outperforms that of the Google Document Text Detection API by 8% on the processed images.   

At the bottom, the average character accuracy for all the models as well as the number of perfectly OCRed samples are computed.  

**Ensemble Accuracy** -- Each column gives the accuracy of the corresponding model on each of the 75 test images. Considering the first column, we see that Tesseract, without any training, has a 55% character accuracy on the test set. Comparing the third through tenth columns with the first, we see that fine-tuning Tesseract on dot matrix fonts increases the character accuracy to 65-70%. The second column shows that the Google Document Text Detection API has an average character accuracy of 79% on the test set. 

The eleventh column reveals that, by ensembing the Google Document Text Detection API with the eight fine-tuned Tesseract models, we can achieve an average character accuracy of 87% on the test set. The twelfth column shows that the best possible character accuracy that could theoretically have been achieved by such an ensemble is 89%. The thirteenth column shows how many of the models achieved the best possible accuracy. 

The eleventh column is also color-coded to highlight its performance on each example. A dark blue accuracy means that the ensemble achieved the unique best accuracy on that example. A light blue accuracy means that the ensemble achieved the best possible accuracy on that example, but the best accuracy was not unique. An orange accuracy means that the ensemble achieved an accuracy strictly between the best and the worst possible accuracies. A red accuracy means that the ensemble chose the worse possible accuracy.

At the bottom, the average character accuracy for all the models as well as the number of perfectly OCRed samples are computed.  

**Comparison Google Text Detection versus Tesseract Ensemble** -- The first column gives the results for the Google Text Detection API with no image processing. The second column gives the results for the pure Tesseract ensemble with no image processing. Comparing the first and second columns, we see that the pure Tesseract ensemble's character accuracy outperforms that of the Google Text Detection API by 12% on the raw images. 

The third column gives the results of the Google Text Detection API with my image processing. Comparing with the first column, we see that my image processing increases the average character accuracy by 6%. 

The last column gives the results for the pure Tesseract ensemble with my image processing. Comparing with the third column, we see that the pure Tesseract ensemble's character accuracy outperforms that of the Google Text Detection API by 9% on the processed images. Comparing with the second column, we see that my image processing increases the average character accuracy by 3%.   

At the bottom, the average character accuracy as well as the number of perfectly OCRed samples are computed.

**Average Confidence** -- Each column gives the confidence of the corresponding model on each of the 75 test images. At the bottom, the average confidence across all 75 test examples are computed for all the models.

## Image-processing pipeline

ocr_preprocess.py -- This program does all the image processing that Tesseract desires such as rescaling, binarisation, deskewing, and removing alpha channel.

ocr_preprocess_image.py -- Does image processing for dark images when OTSU does not work so well.

## Testing framework

GoogleAPI.py -- Writes Google Text Detection API OCR output to output directory as .txt files for images in input directory

GoogleDocAPI.py -- Writes Google Document Text Detection API OCR output to output director as .txt files for images in input directory.

ocr_confidences.py: Outputs average confidence of each model in Tesseract ensemble for each image.

myaccsummary.sh: Given a directory that contains ground truth text files as well as OCR output text files and images, outputs the average character accuracy.

tessaccsummary: Given a directory containing images and ground truth text files as well as a .traineddata file, evaluates outputs the average character accuracy of the tesseract model.

images.zip -- Contains 75 raw images of real dot matrix fonts in the wild along with their accompanying ground truth text files

images_processed.zip -- Contains 75 processed images of real dot matrix fonts in the wild along with their accompanying ground truth text files. The images are the images from images.zip processed with ocr_preprocess.py and 
ocr_preprocess_image.py

GplusTRaw.zip -- Contains the gplust_ensemble.py OCR outputs of the images in images.zip as well as all the contents of images.zip

GplusTProcessed.zip -- Contains the gplust_ensemble.py OCR output of the images in images_processed.zip as well as all the contents of images_processed.zip 

TessProcessed.zip -- Contains the tesseract_ensemble.py OCR output of the images in images_processed.zip as well as all the contents of images_processed.zip

TessRaw.zip -- Contains the tesseract_ensemble.py OCR outputs of the images in images.zip as well as all the contents of images.zip

GoogleRaw.zip -- Contains the Google Text Detection API OCR outputs of the images in images.zip as well as all the contents of images.zip

GoogleProcessed.zip -- Contains the Google Text Detection API OCR outputs of the images in images_processed.zip as well as all the contents of images_process.zip

GoogleDocRaw.zip -- Contains the Google Document Text Detection API OCR output of the images in images.zip as well as all the contents of images.zip

GoogleDocProcessed.zip -- Contains the Google Document Text Detection API OCR output of the images in images_processed.zip as a well as all the content of images_processed.zip

## Custom dot-matrix font dataset used to create the most successful model in the Tesseract ensemble

Dot_Matrix_Test_1: Contains a custom dataset for dot matrix fonts that was used to train dotOCRDData1.traineddata, the most successful model in the Tesseract ensemble.  This model was trained using ocrd-train, which is not the standard Tesseract training procedure.  The classes are 0-9, A-Z, Colon, Dash, Period, Slash. The images were created by either deleting or perturbing a dot in a character.

Dot_Matrix_Font_Generator_2.ipynb: Code for creating the dataset in Dot_Matrix_Test_1

automake.sh -- Creates the directory Dot_Matrix_Test_n and creates subdirectories for each of the classes 0-9, A-Z, Colon, Dash, Period, Slash

autocount.sh -- Changes into the directory Dot_Matrix_Test_n and counts the number of .tiff images for each of the classes 0-9, A-Z, Colon, Dash, Period, Slash.

automove.sh -- From each subdirectory in Dot_Matrix_Test_n, moves all .tiff files to the corresponding directory in Dot_Matrix_Test_m

autogt.sh -- Changes into the directory Dot_Matrix_Test_n and creates a .gt.txt transcription file for each .tif file in each of the subdirectories 0-9, A-Z, Colon, Dash, Period, Slash.

automovegt.sh -- From each subdirectory in Dot_Matrix_Test_1, moves all files to the ground truth directory

autoprocess.sh -- Changes into the directory Dot_Matrix_Test_n Processes all the .tiff files so they can be read by Tesseract without error

autorename.sh -- Changes into the directory Dot_Matrix_Test_n Renames all the .tiff files to .tif files





