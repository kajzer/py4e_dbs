#!/usr/bin/env python3
# pdf_combine.py - combine many pdfs from current working directory into single one

import PyPDF2, os, glob
from PyPDF2 import PdfFileMerger

def main():
    # Get all the PDF filenames
    pdfFiles = []
    
    # FIRST WAY TO GET ALL FILES
    # for filename in os.listdir('.'):
    #     if filename.endswith('.pdf'):
    #         pdfFiles.append(filename)
    
    # SECOND WAY WITH GLOB
    # for filename in glob.glob('*.pdf'):
    #     pdfFiles.append(filename)
    
    # THIRD WAY WITH COMPREHENSION
    pdfFiles = [filename for filename in glob.glob('*.pdf')]
    pdfFiles.sort(key=str.lower)
    # pdfWriter = PyPDF2.PdfFileWriter()
    merger = PdfFileMerger()
    
    # Loop through all the PDF files
    for filename in pdfFiles:
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
        # FIRST WAY TO GET PAGES
        # Loop through all the pages (except the first) and add them. One by one
        # for pageNum in range(1, pdfReader.numPages):
        #   pageObj = pdfReader.getPage(pageNum)
        #   pdfWriter.addPage(pageObj)
           
        # SECOND WAY TO GET PAGES FROM DOCUMENTATION OF PyPDF2 USING MERGER
        merger.append(fileobj = pdfFileObj, pages=(1, pdfReader.numPages))
    
    # Save the resulting PDF to a file.
    pdfOutput = open('allminutes.pdf', 'wb')
    merger.write(pdfOutput)
    pdfOutput.close()
    
if __name__ == "__main__":
    main()