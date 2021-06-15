# importing required modules 
# First install the PDF package
# pip install docx2txt
#import the library
import docx2txt
import PyPDF2
import io
import codecs
import os


#convert docx to txt
def docx(docxname,txtname):
    """docstring goes here""""
# replace following line with location of your .docx file
    MY_TEXT = docx2txt.process("ram/"+docxname)
    txtfile=txtname+str(".txt")
    f= codecs.open(txtfile,"w+","utf-8")
    f.write(MY_TEXT)
    f.close()
    
    
#convert pdf to txt
def pdf(pdfname,txtname):
    """docstring goes here""""
    pdf = PyPDF2.PdfFileReader (open("ram/"+str(pdfname),"rb"))
    txtfile=txtname+str(".txt")
    #Open the new TEXT file
    f= codecs.open(txtfile,"w+","utf-8")
    for page in pdf.pages:
        # print (page.extractText())
        f.write(page.extractText())
    f.close()
    
   
#read the files path
def ram():
    """docstring goes here""""
    entries = os.listdir('ram/')
    for entry in entries:
        # print(entry)
        files=os.path.splitext(entry)
        print(files[0],files[1])

        '''in any model of the bag.the model is first taken and printed it 
    and printed it and enter it to send it back'''
        if str(files[1])==".pdf":
            pdf(entry,str(files[0]))
            print("pdf")
        if str(files[1])==".docx":
            docx(entry,str(files[0]))
            print("docx")
ram()        

