import PyPDF2


def overlap_wtrmrk(name_pdf1_wtrmrk, name_pdf2, name_pdf_out):
    with open(f'./PDFs/{name_pdf1_wtrmrk}.pdf', 'rb') as my_file_1:
        reader1 = PyPDF2.PdfFileReader(my_file_1)
        # tbm se pode fazer PyPDF2.PdfFileReader(open('./PDFs/wtr.pdf', 'rb'))
        page_wtr = reader1.getPage(0)
        with open(f'./PDFs/{name_pdf2}.pdf', 'rb') as my_file_2:
            reader2 = PyPDF2.PdfFileReader(my_file_2)
            total_pages = reader2.getNumPages()
            writer = PyPDF2.PdfFileWriter()
            i = 0
            while i < total_pages:
                page_doc = reader2.getPage(i)
                page_doc.mergePage(page_wtr)
                writer.insertPage(page_doc, i)
                i += 1
            with open(f'./PDFs/{name_pdf_out}.pdf', 'wb') as new_file:
                writer.write(new_file)


def extract_pages(name_pdf_in, name_pdf_out, *pages):
    with open(f'./PDFs/{name_pdf_in}.pdf', 'rb') as my_file_1:
        reader1 = PyPDF2.PdfFileReader(my_file_1)
        writer = PyPDF2.PdfFileWriter()
        i = 0
        for page in pages:
            page_doc = reader1.getPage(f'{page}')
            writer.insertPage(page_doc, i)
            i += 1
        with open(f'./PDFs/{name_pdf_out}.pdf', 'wb') as new_file:
            writer.write(new_file)


def merge_pdfs(name_pdf_out, *name_pdfs_in):
    writer = PyPDF2.PdfFileWriter()
    i = 0
    for name_pdf in name_pdfs_in:
        with open(f'./PDFs-1/{name_pdf}.pdf', 'rb') as my_file_1:
            reader1 = PyPDF2.PdfFileReader(my_file_1)
            total_pages = reader1.getNumPages()
            z = 0
            while z < total_pages:
                page_doc = reader1.getPage(z)
                writer.insertPage(page_doc, i)
                i += 1
                z += 1
            #we could add a guard so we don't write at every iteration    
            with open(f'./PDFs-1/{name_pdf_out}.pdf', 'wb') as new_file:
                writer.write(new_file)

