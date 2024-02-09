from PyPDF2 import PdfReader


class ResumeReader:
    pathVar = ""

    def readPDF(path):
        reader = PdfReader(path)
        extracted_text = ""
        for page in reader.pages:
            extracted_text += page.extract_text()
        return extracted_text
