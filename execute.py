import code.PdfReader as PdfReaderModule
import code.ExcelReader as ExcelReader
import code.TemplateParser as TemplateParser
import code.PdfAnalyzer as PdfAnalyzer

def main():
    # TODO Do not forget, to remind user, that [MONTH] should be updated before continueing!
    print("If you use [MONTH] in you template, don't forget to update it in InvoiceSenderControl.xlsx")
    input("Press Enter to continue... (close window with script to CANCEL)")
    print("Parsing excel...")
    excelReader = ExcelReader.ExcelReader()
    excelContent = excelReader.getData()
    
    print("Parsing pdf...")
    pdfReader = PdfReaderModule.PdfReader()
    pdfFileNameToItsContentMap = pdfReader.getReadedInvoicesMap()
    
    print("Searching pdfs...")
    pdfAnalyzer = PdfAnalyzer.PdfAnalyzer(pdfFileNameToItsContentMap)
    
    # pdfAnalyzer.searchSentenceAndUpdateStats() # searchedSentence
    #templateParser = TemplateParser.TemplateParser( ) # templateText, keywordsMap
    #emailFilledTemplate = templateParser.getFilledTemplate()
    
    print("Checking if all PDFs can be delivered:")
    pdfAnalyzer.dropStatistics()
    input("Press Enter to send emails.. (close window with script to CANCEL)")
    print("Sending emails")

if __name__ == '__main__':
    main()
