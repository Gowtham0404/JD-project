# importing required modules 

import docx2txt
import PyPDF2
import io
import codecs
import os
import glob
import win32com.client



#convert docx to txt

def docx(docxname,txtname):


    MY_TEXT = docx2txt.process("ram/"+docxname)
    txtfile=txtname+str(".txt")
    f= codecs.open(txtfile,"w+","utf-8")
    f.write(MY_TEXT)
    f.close()


#convert pdf to txt

def pdf(pdfname,txtname):


    pdf = PyPDF2.PdfFileReader (open("ram/"+str(pdfname),"rb"))
    txtfile=txtname+str(".txt")
    #Open the new TEXT file
    f= codecs.open(txtfile,"w+","utf-8")
    for page in pdf.pages:
        # print (page.extractText())
        f.write(page.extractText())
    f.close()



def doc():
    word = win32com.client.Dispatch("Word.Application")
    word.visible = 0
    for i, doc in enumerate(glob.iglob("*.doc")):
        in_file = os.path.abspath(doc)
        wb = word.Documents.Open(in_file)
        print(in_file)
        out_file = str(in_file)[:-4] + ".docx"
        print(out_file)
        wb.SaveAs2(out_file, FileFormat=16) # file format for docx
        wb.Close()
    word.Quit()

#read the files path
def ram():


    entries = os.listdir('ram/')
    for entry in entries:

        files=os.path.splitext(entry)
        print(files[0],files[1])
        if str(files[1])==".pdf":
            pdf(entry,str(files[0]))
            print("pdf")
        if str(files[1])==".docx":
            docx(entry,str(files[0]))
            print("docx")
ram()        
doc()

