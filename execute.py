import code.PdfReader as PdfReaderModule
import code.ExcelReader as ExcelReader
import code.TemplateParser as TemplateParser
import code.PdfAnalyzer as PdfAnalyzer
import code.EmailSender as EmailSender

def getFileContent(fileName):
    read_data = ""
    with open(fileName, encoding="utf-8") as f:
        read_data = f.read()
    return read_data

def main():
    # TODO Do not forget, to remind user, that [MONTH] should be updated before continueing!
    print("If you use [MONTH] in you template, don't forget to update it in InvoiceSenderControl.xlsx")
    input("Press Enter to continue... (close window with script to CANCEL)")
    print("Parsing excel...")
    excelReader = ExcelReader.ExcelReader()
    excelContent = excelReader.getData()
    excelSmtpData = excelReader.getSmtpData()
    
    print("Parsing pdf...")
    pdfReader = PdfReaderModule.PdfReader()
    pdfFileNameToItsContentMap = pdfReader.getReadedInvoicesMap()
    
    print("Searching pdfs...")
    pdfAnalyzer = PdfAnalyzer.PdfAnalyzer(pdfFileNameToItsContentMap)

    emailContentAttachmentList = []

    for (invoiceText, emailAddress, templateName, keyWordMap, emailSubject, messageId) in excelContent:
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

        emailContentAttachmentList.append( (emailAddress, emailSubject, emailFilledTemplate, invoicesToAttach, messageId) )


    print("What will be sent:")
    for (emailAddress, emailSubject, emailFilledTemplate, invoicesToAttach, messageId) in emailContentAttachmentList:
        print("To " + emailAddress + " will be send " + str(invoicesToAttach))
    
    print("Checking if all PDFs can be delivered:")
    pdfAnalyzer.dropStatistics()
    input("Press Enter to send emails.. (close window with script to CANCEL)")
    print("Sending emails...")

    (smtpAddress, smtpPort, ownerEmail, ownerPassword) = excelSmtpData
    emailSender = EmailSender.EmailSender(smtpAddress, smtpPort, ownerEmail, ownerPassword)
    for (emailAddress, emailSubject, emailFilledTemplate, invoicesToAttach, messageId) in emailContentAttachmentList:
        if messageId == None or messageId == "":
            emailSender.sendEmail(emailAddress, emailSubject, emailFilledTemplate, invoicesToAttach)
            print("Sent an email to " + emailAddress + " with " + str(invoicesToAttach))
        else:
            emailSender.replayEmail(emailAddress, emailSubject, emailFilledTemplate, invoicesToAttach, messageId)
            print("Sent response to " + emailAddress + " with " + str(invoicesToAttach))
        
    emailSender.close()

if __name__ == '__main__':
    main()
