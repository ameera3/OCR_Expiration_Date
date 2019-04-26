# import the necessary packages
import io
import argparse
import os
import glob
import numpy as np

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="My_First_Project.json"

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
    transcripts = ""
    count = 0
    confidences = []
    numChars = []
    avg_confidence = -1
    Slash_Flag = 0
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    count = count + 1
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                        ])
                    if( count == 1 or Slash_Flag == 1 or word_text == "/" or word_text == "-" ):
                        transcripts = transcripts + word_text
                    else:
                        transcripts = transcripts + " " + word_text
                    if( word_text == "/" or word_text == "-"):
                        Slash_Flag = 1;
                    else:
                        Slash_Flag = 0;
                    confidences.append(word.confidence)
                    numChars.append(len(word_text))
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))     
    transcripts = transcripts + "\n"             
    if confidences != []:
        avg_confidence = np.average(confidences, weights=numChars) 
    return (transcripts, avg_confidence);                

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_dir", help="Input directory for the files to be modified")
ap.add_argument("-o", "--output_dir", help="Output directory for the files to be modified")
args = vars(ap.parse_args())

input_dir = args["input_dir"]
output_dir = args["output_dir"]

im_names = sorted(glob.glob(os.path.join(input_dir, '*.png')))

for im_name in im_names:
    file_name = os.path.basename(im_name).split('.')[0]
    file_name = file_name.split()[0]
    print(file_name)
    print('\n')
    (text, avg_confidence) = detect_text(im_name)
    save_path = os.path.join(output_dir, file_name + ".txt")
    f = open(save_path, "w")
    f.write(text)
    print(text)
    print('\n')
    print(avg_confidence)


