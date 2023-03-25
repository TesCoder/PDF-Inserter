# This program inserts a PDF into every other page of another PDF.
# requires PyPDF2; install with "pip install PyPDF2" or "pip3 install PyPDF2 "

#!/usr/local/bin/python3
from PyPDF2 import PdfReader, PdfWriter

print("This program inserts an insert PDF into another (main) file in every other page.")

def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()

    mainFile = paths[0]
    insertFile = paths[1]

    insertFile_pdf_reader = PdfReader(insertFile)
    insert = insertFile_pdf_reader.pages[0]

    for i in range(1):
        pdf_reader = PdfReader(mainFile)
        # for page in range(pdf_reader.getNumPages()):
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(insert)
            pdf_writer.add_page(pdf_reader.pages[page])


    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
def main():
    print("This program inserts a PDF into every other page of another PDF.")
    file1 = input("Enter the main file: ")
    file2 = input("Enter the indert PDF file: ")
    paths = [file1, file2]
    merge_pdfs(paths, output='merged.pdf')


main()
