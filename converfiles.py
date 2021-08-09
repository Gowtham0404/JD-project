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


#covert doc to docx

def pdf(pdfname,txtname):
    try:
        
        outfile = codecs.open(outfolder+outfile,'w+',"utf-8")
        app.visible = False
        wb = app.Documents.Open(pathsdoc+str(infile))
        doc = app.ActiveDocument
        outfile.write(doc.Content.Text)
    except Exception as e:
        print(e)
    finally:
        outfile.close()
        app.Quit()

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
        if str(files[0],files[1])
            doc(entry,str(files[0])) 
            print("doc")  
            
ram()        
doc()