# Image-to-Text Converter
> This Python script extracts texts from multiple image files, combines the texts and saves them in txt and MS docx file types.


## Prerequisites
The following dependencies are required to run this script


* Python 3
* Pillow (PIL) library
* pytesseract library
* Tesseract OCR engine
* docx library
- On VsCode Terminal
    Install Pillow, an image processing library in python, using this command

        `pip install pillow`
    Install tesserct-ocr using this command

        `sudo apt install tesseract-ocr`
    Install pytesseract, Python wrapper for tesserct-ocr using this command

        `pip install pytesseract`
    Install docx, a library that allows creating and updating MS Word (.docx) files.

        `pip install python-docx`

## Usage
- Clone or download this repository to your local machine.
- Place your image files in the imagetotxt folder.
- List the names of the image files you want to convert in the ordered.txt file, this is in the order you want the images to be processed.
- Run the script using the following command:
        `/bin/python3 /your_directory/TextGenerator-Tesseract/image_example.py`
- The output will be saved in output.txt and output.docx files.


## Additional Notes
- I have only included images in JPEG, JPG, and PNG format.
- You can read more on [Tesseract Documentation](https://tesseract-ocr.github.io/tessdoc/)
