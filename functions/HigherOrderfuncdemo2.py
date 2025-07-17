
def pdfHandler():
    print(f"pdf handler called...")

def imageHandler():
    print(f"image handler called...")    

def docHandler():
    print(f"doc handler called...")


#cb == callback...
def handleFile(cb):
    print("hanlde file function called...")
    cb() # cb == imagehandler

# handleFile(imageHandler)

fileName = "abc.doc"

if fileName.endswith(".pdf"):
    handleFile(pdfHandler)
elif fileName.endswith(".doc"):
    handleFile(docHandler)    
elif fileName.endswith(".jpg"):
    handleFile(imageHandler)    
