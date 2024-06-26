# -*- coding: utf-8 -*-
"""ocralgorithm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KIN2YJzHR5yEfh9kkRTDTvZJQSfZggvY
"""

!pip install pytesseract
!sudo apt-get install tesseract-ocr
!pip install opencv-python

import cv2
import pytesseract
import csv
from google.colab import files

# install as it will be used
!sudo apt-get install tesseract-ocr

# path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def preprocess_image(image):
    ## pre process image and convert it to graycode
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return threshold

def extract_text_from_image(image):
    ## extract text from image
    preprocessed_image = preprocess_image(image)
    return pytesseract.image_to_string(preprocessed_image)

def detect_table(image):

    ## after converting image to gray code now its time to detect table from it
    height, width = image.shape[:2]
    table_region = [(0, 0), (width, height)]
    return [table_region]

def extract_table_data(image, table_region):
    x1, y1 = table_region[0]
    x2, y2 = table_region[1]
    table_image = image[y1:y2, x1:x2]

    # Extract text from the table image
    table_text = extract_text_from_image(table_image)
    return table_text
def write_to_csv(data, output_file):

    ## detect if column is already there then use it instead of creating new one
    transposed_data = list(map(list, zip(*data)))

    # open output file and use csv.writer
    with open(output_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for column in transposed_data:
            column_exists = False
            # Check if the column already exists in the CSV
            with open(output_file, 'r') as csvfile_read:
                reader = csv.reader(csvfile_read)
                for existing_row in reader:
                    if column == existing_row:
                        column_exists = True
                        break
            # if the column exists, append an empty row and then the new column below it
            if column_exists:
                writer.writerow([''] * len(column))  # Add an empty row
            writer.writerow(column)

def main(image_path, output_csv):
    ## below algortihm reads the image using cv2
    image = cv2.imread(image_path)

    ## there is detect table function above that detect table from the image
    table_regions = detect_table(image)

    ## extract data from each table region and write to csv file
    for i, table_region in enumerate(table_regions):
        table_data = extract_table_data(image, table_region)
        data = [line.split('\n') for line in table_data.split('\n\n')]
        write_to_csv(data, output_csv)
        print(f"Table {i+1} extracted and written to CSV.")

## upload image from which the table or data is to be extracted
uploaded = files.upload()
for filename in uploaded.keys():
    print('Uploaded file:', filename)
    main(filename, 'output_data.csv')

## csv files are saved in browser to downoad it run below code
from google.colab import files
files.download('output_data.csv')