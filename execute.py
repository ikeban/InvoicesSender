import code.PdfReader as PdfReaderModule
import code.ExcelReader as ExcelReader
import code.TemplateParser as TemplateParser
import code.PdfAnalyzer as PdfAnalyzer


def getFileContent(fileName):
    read_data = ""
    with open(fileName) as f:
        read_data = f.read()
    return read_data

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

    emailContentAttachmentList = []

    for (invoiceText, emailAddress, templateName, keyWordMap) in excelContent:
        invoicesToAttach = pdfAnalyzer.searchSentenceAndUpdateStats(invoiceText)
        if len(invoicesToAttach) == 0:
            print("No invoices for: " + emailAddress + " SKIPPING!")
            continue  
        
        templateContent = getFileContent("emailTemplates/" + templateName)
        if templateContent is None or templateContent == "":
            print("template not existing or empty for: " + emailAddress + " SKIPPING!")
            continue
        templateParser = TemplateParser.TemplateParser(templateContent, keyWordMap)
        emailFilledTemplate = templateParser.getFilledTemplate()

        emailContentAttachmentList.append( (emailAddress, emailFilledTemplate, invoicesToAttach) )
        
    


    print("What will be sent:")
    for (emailAddress, emailFilledTemplate, invoicesToAttach) in emailContentAttachmentList:
        print("To " + emailAddress + " will be send " + str(invoicesToAttach))
    
    print("Checking if all PDFs can be delivered:")
    pdfAnalyzer.dropStatistics()
    input("Press Enter to send emails.. (close window with script to CANCEL)")
    print("Sending emails")

if __name__ == '__main__':
    main()
