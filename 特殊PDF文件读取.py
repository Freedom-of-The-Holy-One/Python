# coding=utf-8
# PDF格式文件转换
# Python中pdfminer的使用
# 因为库的原因,只能处理一些特殊的PDF文件;一些特殊文本无法读取

# 打开一个PDF文件
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter

from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator

fp=open("Test/Web.pdf","rb")
# 创建一个与文件关联的PDF对象
parse=PDFParser(fp)
# 创建一个存储文档结构的PDF文档对象
document=PDFDocument(parse)
# 创建一个存储共享资源的PDF资源管理器对象
resource_Manage=PDFResourceManager(caching=False)
# 创建PDF设备对象
# device=PDFDevice(resource_Manage)
# 设置分析参数
paramer=LAParams()
# 创建PDF页面聚合器对象
device=PDFPageAggregator(resource_Manage,laparams=paramer)
# 创建PDF解释器对象
interpreter = PDFPageInterpreter(resource_Manage, device)
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout=device.get_result()
    for text in layout:
        print text.get_text()
