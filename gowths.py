import PyPDF2
import io
import codecs
#Read the PDF file
#inside the PDF path
pdf = PyPDF2.PdfFileReader (open("pdfs/asycio.pdf","rb"))
f= codecs.open("guru99.txt","w+","utf-8")
for page in pdf.pages:
  print (page.extractText())
  f.write(page.extractText())
f.close()