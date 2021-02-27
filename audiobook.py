import PyPDF2
path=input("Enter the file path of the pdf ")
pdfFileObject = open(path, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
print(" No. Of Pages in the pdf :", pdfReader.numPages)
txt=""
for i in range(pdfReader.numPages):
    pageObject = pdfReader.getPage(i)
    txt+=pageObject.extractText()
#print(txt)
from gtts import gTTS
import os
lan='en'
myobj=gTTS(text=txt,lang=lan,slow=False)
myobj.save("audiobook.mp3")
print("mp3 file is created ")
pdfFileObject.close()