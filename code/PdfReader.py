from pdfminer.high_level import extract_text
import os

class PdfReader:
    """ Read all invoices in invoices directory """
    def __init__(self):
        self._invoiceMap = {}
        self._loadAllPdfContent()

    def getReadedInvoicesMap(self):
        return self._invoiceMap

    def _loadAllPdfContent(self):
        allPdfFiles = self._getAllInvoicesNames()
        for pdfFile in allPdfFiles:
            fileContent = self._readDataFromOnePDf("invoices/"  + pdfFile)
            self._invoiceMap["invoices/"  + pdfFile] = fileContent

    def _readDataFromOnePDf(self, pdfFileName):
        pdfFileObject = open(pdfFileName, 'rb')
        pdfContent = extract_text(pdfFileObject)
        return pdfContent
    
    def _getAllInvoicesNames(self):
        fileList = os.listdir('invoices')
        try:
            fileList.remove('HERE_PUT_YOUR_INVOICES.txt')
        except ValueError:
            pass
        return fileList
