import PyPDF2

def extract_text_from_pdf(pdf_path):

    text = ""

    with open(pdf_path, 'rb') as file: #open the pdf file in binary mode  #rd use to read the file in text mode, rb is used to read the file in binary mode
        reader = PyPDF2.PdfReader(file) # create a PdfReader object to read the pdf file #This loads the PDF so Python can read it.

        for page in reader.pages:   #loop through each page in the PDF and extract text from it #This loops through each page of the PDF and extracts the text from it.
            text += page.extract_text()

    return text