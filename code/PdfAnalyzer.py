class PdfAnalyzer:
    """ Pick PDFs with specified sentence.
        This class also detects not sent invoices,
            and invoices delivered to two (more) recipents. 
    """
    def __init__(self, pdfNameToContentMap):
        """
            Input is map. PDF file names are mapped to its content.
        """
        self._pdfNameToContentMap = pdfNameToContentMap
        self._pdfStatistics = {}
        for pdfFileNames in pdfNameToContentMap:
            self._pdfStatistics[pdfFileNames] = 0

    def searchSentenceAndUpdateStats(self, searchedSentence):
        pdfsContainingSearchSentence = []
        for fileName, fileContent in self._pdfNameToContentMap.items():
            if fileContent.find(searchedSentence) != -1:
                self._pdfStatistics[fileName] += 1
                pdfsContainingSearchSentence.append(fileName)
        return pdfsContainingSearchSentence
                

    def dropStatistics(self):
        for fileName, numberOfReferences in self._pdfStatistics.items():
            if numberOfReferences != 1:
                print("File " + fileName + " has number of reference equal to: " + str(numberOfReferences))
