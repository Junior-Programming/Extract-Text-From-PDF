from PyPDF2 import PdfReader

reader = PdfReader(
    "D:/Materi pembelajaran individu/Programing/Project Python/5. Extract Text from a PDF/test.pdf")
page = reader.pages[0]
print(page.extract_text())
