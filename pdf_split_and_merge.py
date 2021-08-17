# pdf_split and_merge.py
# need PyPDF2 libary
import os, sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

# 拆分选中pdf页码为单页
def pdf_split(file, page):
    pdf = PdfFileReader(open(file, "rb"))
    for i in range(pdf.numPages):
        if type(page)==type(0):
            output = PdfFileWriter()
            output.addPage(pdf.getPage(i))
            with open(file.replace(".pdf", "")+"_page%s.pdf" % i, "wb") as outputStream:
                output.write(outputStream)
            continue
        if type(page)==type([0]):
            if i in page:
                output = PdfFileWriter()
                output.addPage(pdf.getPage(i))
                with open(file.replace(".pdf", "")+"_page%s.pdf" % i, "wb") as outputStream:
                    output.write(outputStream)

# 按文件夹里面的pdf顺序将几个pdf合并为一个pdf           
def pdf_merge(file):
    pdf_list = []
    for f in os.listdir(file):
        if f.endswith('.pdf'):
            pdf_list.append(f)
    pdf_list = [os.path.join(file, filename) for filename in pdf_list]
    file_merge = PdfFileMerger()
    for pdf in pdf_list:
        file_merge.append(pdf)
    file_merge.write("".join(file.split("\\")[:-1])+file.split("\\")[-1]+".pdf")

# 主程序 
def Main():
    if sys.argv[1]=="merge":
        pdf_merge(sys.argv[2].replace("\\", "/"))
    elif sys.argv[1]=="split":
        if len(sys.argv)==4:
            pdf_split(sys.argv[2].replace("\\", "/"), int(sys.argv[3]))
        elif len(sys.argv)==5:
            page = list(range(int(sys.argv[-2])-1, int(sys.argv[-1])))
            pdf_split(sys.argv[2].replace("\\", "/"), page)
    else:
        print("Command error!")

if __name__=="__main__":
    Main()