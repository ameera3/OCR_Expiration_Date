# Usage: python GoogleAPI.py -i /home/images -o /home/GoogleRaw
# Outputs the GoogleAPI ocr into text files  
# import the necessary packages
import io
import argparse
import os
import glob

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="My_First_Project.json"

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    transcripts = ""
    count = 0
    for text in texts:
        count = count + 1
        transcript= text.description
        transcripts = transcripts + transcript
        if count == 1:
            break
    return transcripts

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
    text = detect_text(im_name)
    save_path = os.path.join(output_dir, file_name + ".txt")
    f = open(save_path, "w")
    f.write(text)
    print(text)
    print('\n')

    
    


