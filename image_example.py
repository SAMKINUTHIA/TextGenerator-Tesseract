from PIL import Image
import pytesseract
import os

# Define the directory containing the images
dir_path = "/home/linux/TextGenerator-Tesseract/"
# Define Block separator
separator = "=" * 50  # 50 dashes

output_text = ''

with open('ordered.txt', 'r') as f:
    filenames = [line.strip() for line in f.readlines()]


# Loop through all files in the directory
for filename in filenames:
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Open the image file
        im = Image.open(os.path.join(dir_path, filename))

        # Extract text from the image
        text = pytesseract.image_to_string(im, lang='eng').strip() + '\n' + separator + '\n'
        
        # Add the text to the output text
        output_text += text
        
# Write the output text to the output file
with open('output.txt', "w") as f:
    f.write(output_text)


#Converting the generated text to word document
import docx

# Open the text file
with open('output.txt', 'r') as file:
    text = file.read()

# Create a new Word document
doc = docx.Document()

# Add the text to the document
doc.add_paragraph(text)

# Save the document as a Word file
doc.save('output.docx')
