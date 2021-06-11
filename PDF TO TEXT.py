# First install the PDF package
pip install PyPDF2
#import the library
import PyPDF2
#Read the PDF file
#inside the PDF path
pdf = PyPDF2.PdfFileReader (open("/content/drive/MyDrive/Student_AFD_8885488_492018144248773.pdf","rb"))
for page in pdf.pages:
  print (page.extractText());