import PyPDF2

pdfFileObj = open('SwiffgJpn.pdf','rb')   

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num=pdfReader.numPages

for a in range(0, num):
    pageObj = pdfReader.getPage(a)         
    text=pageObj.extractText().encode('utf-8')
    print(text)
