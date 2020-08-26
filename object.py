import PyPDF2

class pdf:
    def __init__(self, name, path):
        self.name, self.path = name, path
    

    def open_myfile_read(self):
        with open(self.path, "rb") as self.name:
            reader = PyPDF2.PdfFileReader(self.name, strict=False)
            print(reader.getNumPages()) 
            


