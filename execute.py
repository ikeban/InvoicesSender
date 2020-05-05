import code.PdfReader as PdfReaderModule

def main():
    # TODO Do not forget, to remind user, that [MONTH] should be updated before continueing!
    print("Parsing excel")
    pdfReader = PdfReaderModule.PdfReader()
    print(pdfReader.getReadedInvoicesMap())

if __name__ == '__main__':
    main()
