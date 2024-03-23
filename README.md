# ImageToTable
This Python code performs Optical Character Recognition (OCR) on an uploaded image using the Tesseract OCR library. The code allows users to upload an image file in a Google Colab notebook. After uploading, the image is processed to extract text using Tesseract OCR. The extracted text is then split into rows and saved to a CSV file.

In this modified version, the writing part of the code is enhanced. It checks each row of data before writing it to the CSV file. If a similar row already exists in the CSV, the new row is appended below the existing row. This prevents duplication of identical rows and ensures that similar data is grouped together in the CSV file.

Overall, this code simplifies the process of performing OCR on images and organizing the extracted text into a CSV file, making it easier to manage and analyze textual data from images.
You can even download the csv file generated

Both version in .py and .ipynb is uploaded to run .py you need to install :

1)tesseract-ocr

2)pytesseract

3)cv2

4)import csv


Total five images are present and one sample output file output_file.csv is there which is how the data is as input
