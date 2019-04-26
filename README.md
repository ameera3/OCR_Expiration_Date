# Expiration_Date
Our team designs software for the Department of Homeland Security’s Next Generation First Responder program.  When paramedics respond to a medical emergency, they ask the patient about any recent medications she has taken.  Since a patient’s medication influences which procedures or therapies will be administered, correctly recording and communicating the patient’s recent medication is crucial.  Our team is developing optical character recognition (OCR) software that can correctly read vital information from a photo of a medicine bottle, such as the medication’s name, the dose, the lot number and the expiration date.  

Our experiments show that lot numbers and expiration dates are particularly difficult for off-the-shelf OCR engines, such as Tesseract, to read because they are usually written in a dot-matrix font that varies widely from product to product. For example, Tesseract and the Google Text Detection API achieve a 55% and 60% character accuracy respectively on dot matrix fonts. 

To improve the character accuracy and to mitigate the wide variation in dot matrix fonts, we have developed a novel way to ensemble OCR outputs. Our current ensemble consists of the Google Document Text Detection API and four models trained using Tesseract's LSTM neural network. We achieve over 85% character accuracy with 40 out of 75 test samples achieving perfect 100% character accuracy. Further improvement is expected.

The code on Github has four major functions:

1. Creating and supporting the Google+Tesseract ensemble
2. Reporting Results
3. Image-processing pipeline
4. Testing framework
5. Custom dot-matrix font dataset used to create the most successful model in the Tesseract ensemble

Below, all the programs on Github are organized by their function:

## Creating and supporting the Google+Tesseract ensemble

Traineddata Files -- There are four custom dot matrix traineddata files, 5x5_Dots_FT_500.traineddata, DotMatrix_FT_500.traineddata, Dotrice_FT_500.traineddata, dotOCRDData1.traineddata.  These .traineddata files were created by fine-tuning Tesseract’s LSTM neural network on the respective dot matrix fonts.  These are the four models used in the current Tesseract ensemble.

gplust_ensemble.py -- This program produces the Google+Tesseract ensemble output from the Google Document Text Detection API and our four .traineddata files.

tesseract_ensemble.py -- This program produces the Tesseract ensemble output from the four .traineddata files.

dot_training_text.txt -- The training data that is used to fine-tune Tesseract's neural network to the four dot matrix fonts.

Prepare_Training_Text.ipynb -- Used to create dot_training_text.txt

## Reporting Results

Adding Google Document Text Detection to Ensemble -- The first column gives the results for Google Document Text Detection’s API with no image processing.  The second column gives the results of my Google + Tesseract ensemble with no image processing.  The third column gives the results for Google’s Document Text Detection API with my image processing.  The last column gives the results for my Google + Tesseract ensemble with my image processing. At the bottom, the average character accuracy as well as the number of perfectly OCRed samples are computed.  For the ensemble columns, a red percentage mean that the ensemble performed worse than Google on this example (compare with the column on the left).  Similarly, a green percentage in an ensemble column means that the ensemble performed better than Google on this example. 

Comparison Google Text Detection versus Tesseract Ensemble -- The first column gives the results for the Google Text Detection API with no image processing. The second column gives the results of the Google Text Detection API with my image processing. The last column gives the results for my Tesseract ensemble with my image processing. At the bottom, the average character accuracy as well as the number of perfectly OCRed samples are computed. 

## Image-processing pipeline

ocr_preprocess.py -- This program does all the image processing that Tesseract desires such as rescaling, binarisation, deskewing, and removing alpha channel.

ocr_preprocess_image.py -- Does image processing for dark images when OTSU does not work so well.

## Testing framework

GoogleAPI.py -- Writes Google Text Detection API OCR output to output directory as .txt files for images in input directory

GoogleConfAPI.py -- Writes Google Document Text Detection API OCR output to output director as .txt files for images in input directory.

ocr_confidences.py: Outputs average confidence of each model in Tesseract ensemble for each image

myaccsummary.sh: Given a directory that contains ground truth text files as well as OCR output text files and images, outputs the average character accuracy.

tessaccsummary: Given a directory containing images and ground truth text files as well as a .traineddata file, evaluates outputs the average character accuracy of the tesseract model.

images.zip -- Contains 75 raw images of real dot matrix fonts in the wild along with their accompanying ground truth text files

images_processed.zip -- Contains 75 processed images of real dot matrix fonts in the wild along with their accompanying ground truth text files. The images are the images from images.zip processed with ocr_preprocess.py and 
ocr_preprocess_image.py

GplusTRaw.zip -- Contains the gplust_ensemble.py OCR outputs of the images in images.zip as well as all the contents of images.zip

GplusTProcessed.zip -- Contains the gplust_ensemble.py OCR output of the images in images_processed.zip as well as all the contents of images_processed.zip 

TessProcessed.zip -- Contains the tesseract_ensemble.py OCR output of the images in images_processed.zip as well as all the contents of images_processed.zip

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





