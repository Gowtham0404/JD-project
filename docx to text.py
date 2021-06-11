# First install the PDF package
pip install docx2txt
#import the library
import docx2txt

# replace following line with location of your .docx file
MY_TEXT = docx2txt.process("/content/drive/MyDrive/Letterpad.docx")

with open("Output.txt", "w") as text_file:
    print(MY_TEXT)