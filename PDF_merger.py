# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:46:36 2018

@author: olive
"""

import os 
from PyPDF2 import PdfFileMerger
print (os.getcwd())#prints current working directory

pdf_list = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

merger = PdfFileMerger()

for pdf in pdf_list:
    merger.append(open(pdf, 'rb'))

with open('result.pdf', 'wb') as pdf_out:
    merger.write(pdf_out)