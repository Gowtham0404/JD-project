# First install the PDF package
# pip install docx2txt
#import the library
import docx2txt
import PyPDF2
import io
import codecs
import os


def docx(docxname,txtname):
# replace following line with location of your .docx file
    MY_TEXT = docx2txt.process("ram/"+docxname)
    txtfile=txtname+str(".txt")
    f= codecs.open(txtfile,"w+","utf-8")
    f.write(MY_TEXT)
    f.close()

def pdf(pdfname,txtname):
    pdf = PyPDF2.PdfFileReader (open("ram/"+str(pdfname),"rb"))
    txtfile=txtname+str(".txt")
    #Open the new TEXT file
    f= codecs.open(txtfile,"w+","utf-8")
    for page in pdf.pages:
        # print (page.extractText())
        f.write(page.extractText())
    f.close()
def ram():
    entries = os.listdir('ram/')
    for entry in entries:
        # print(entry)
        files=os.path.splitext(entry)
        print(files[0],files[1])

        if str(files[1])==".pdf":
            pdf(entry,str(files[0]))
            print("pdf")
        if str(files[1])==".docx":
            docx(entry,str(files[0]))
            print("docx")
ram()        

