#pip install the python libraries(PyPDF2,io,codecs)

#import the PyPDF2 library to use the PDF to TEXT convert
import PyPDF2

#import the io library to use the input output
import io

#import the codes library to use the encodes and decoders
import codecs

#Read the PDF file
#inside the PDF path
pdf = PyPDF2.PdfFileReader (open("I:\pdf filder","rb"))

#Open the new TEXT file
f= codecs.open("guru99.txt","w+","utf-8")
for page in pdf.pages:
  print (page.extractText())
  f.write(page.extractText())
f.close()