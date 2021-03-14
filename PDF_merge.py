import PyPDF2

with open('./PDFs/wtr.pdf', 'rb') as my_file_1:
    reader1 = PyPDF2.PdfFileReader(my_file_1)
    # tbm se pode fazer PyPDF2.PdfFileReader(open('./PDFs/wtr.pdf', 'rb'))
    page_wtr = reader1.getPage(0)
    with open('./PDFs/super.pdf', 'rb') as my_file_2:
        reader2 = PyPDF2.PdfFileReader(my_file_2)
        total_pages = reader2.getNumPages()
        writer = PyPDF2.PdfFileWriter()
        i = 0
        while i < total_pages:
            page_doc = reader2.getPage(i)
            page_doc.mergePage(page_wtr)
            writer.insertPage(page_doc, i)
            i += 1
        with open('./PDFs/wtrmarked.pdf', 'wb') as new_file:
            writer.write(new_file)
