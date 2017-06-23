# coding=utf-8
# PDF文件分页
# Python中pypdf的使用
from pyPdf import PdfFileWriter, PdfFileReader
import os
# 打开一个PDF文件
# 例：打开一个在当前路径下文件名为test.pdf的文件
file=PdfFileReader(file("test.pdf",'rb'))
# 设置文件存储路径
# output_file=PdfFileWriter()
# 输出PDF文件名
# print file.getDocumentInfo().title
# 获取文件页数
page_number=file.getNumPages()
# 创建分割文件存储路径
if not os.path.exists("Test"):
    os.makedirs("Test")
for i in range(0,page_number):
    output_file = PdfFileWriter()
    output_file.addPage(file.getPage(i))
    output_stream = open("Test/test"+str(i+1)+".pdf", "wb")
    output_file.write(output_stream)
    output_stream.close()

