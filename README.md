# Expiration_Date
Our team designs software for the Department of Homeland Security’s Next Generation First Responder program.  When paramedics respond to a medical emergency, they ask the patient about any recent medications she has taken.  Since a patient’s medication influences which procedures or therapies will be administered, correctly recording and communicating the patient’s recent medication is crucial.  Our team is developing optical character recognition (OCR) software that can correctly read vital information from a photo of a medicine bottle, such as the medication’s name, the dose, the lot number and the expiration date.  

Our experiments show that lot numbers and expiration dates are particularly difficult for off-the-shelf OCR engines, such as Tesseract, to read because they are usually written in a dot-matrix font that varies widely from product to product. Additional difficulties include the curved shape of the vial and glare. Our team will custom train Tesseract’s neural network to recognize lot numbers and expiration dates in dot matrix font. 

Traineddata Files: There are four custom dot matrix traineddata files, 5x5_Dots_FT_500.traineddata, DotMatrix_FT_500.traineddata, Dotrice_FT_500.traineddata, dotOCRDData1.traineddata. You will want to put these files in your tessdata directory (usually /usr/share/tesseract-ocr/4.00/tessdata). These .traineddata files were created by fine-tuning Tesseract's neural network on the respective dot matrix fonts.

dot_training_text.txt -- The training data that is used to fine-tune Tesseract's neural network.

Prepare_Training_Text.ipynb -- Used to create dot_training_text.txt

ocr.py: This program produces the Tesseract ensemble output from the four .traineddata files.

ocr_preprocess.py: This program does all the image processing that Tesseract desires such as rescaling, binarisation, deskewing, and removing alpha channel. See https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality

ocr_preprocess_image.py: Does image processing for dark images when OTSU does not work so well

ocr_confidences.py: Outputs average confidence of each model in ensemble for each image

myaccsummary.sh: Given a directory that contains ground truth text files as well as OCR output text files, outputs the average character accuracy.

tessaccsummary: Given a directory containing images and ground truth text files as well as a .traineddata file, evaluates outputs the average character accuracy of the tesseract model. You will need to fork https://github.com/Shreeshrii/ocr-evaluation-tools

GoogleAPI.py: Writes GoogleAPI OCR output to output directory as .txt files for images in input directory

images.zip: Contains 75 raw images of real dot matrix fonts in the wild along with their accompanying ground truth text files

images_processed.zip: 75 processed images of real dot matrix fonts in the wild along with their accompanying ground truth text files. The images are the images from images.zip processed with ocr_preprocess.py and ocr_preprocess_image.py

GoogleRaw.zip: Contains the GoogleAPI OCR outputs of the images in images.zip as well as all the contents of images.zip

GoogleProcessed.zip: Contains the GoogleAPI OCR outputs of the images in images_processed.zip as well as all the contents of images_process.zip

Dot_Matrix_Test_1: Contains a custom dataset for dot matrix fonts that was used to train dotOCRDData1.traineddata. The classes are 0-9, A-Z, Colon, Dash, Period, Slash. The images were created by either deleting or perturbing a dot in a character.

Dot_Matrix_Font_Generator_2.ipynb: Code for creating the dataset in Dot_Matrix_Test_1

automake.sh -- Usage: ./automake.sh n (where n is an integer). Creates the directory Dot_Matrix_Test_n and creates subdirectories for each of the classes 0-9, A-Z, Colon, Dash, Period, Slash

autocount.sh -- Usage ./autocount.sh n (where n is an integer). Changes into the directory Dot_Matrix_Test_n and counts the number of .tiff images for each of the classes 0-9, A-Z, Colon, Dash, Period, Slash.

automove.sh -- Usage: ./automake.sh n m (where n and m are integers). From each subdirectory in Dot_Matrix_Test_n, moves all .tiff files to the corresponding directory in Dot_Matrix_Test_m

autogt.sh -- Usage: ./autogt.sh n (where n is an integer). Changes into the directory Dot_Matrix_Test_n and creates a .gt.txt transcription file for each .tif file in each of the subdirectories 0-9, A-Z, Colon, Dash, Period, Slash.

automovegt.sh -- Usage: ./automovegt n (where n and m are integers). From each subdirectory in Dot_Matrix_Test_1, moves all files to the ground truth directory

autoprocess.sh -- Usage ./autoprocess n (where n is an integer). Changes into the directory Dot_Matrix_Test_n Processes all the .tiff files so they can be read by Tesseract without error

autorename.sh -- Usage ./autorename n (where n is an integer). Changes into the directory Dot_Matrix_Test_n Renames all the .tiff files to .tif files
