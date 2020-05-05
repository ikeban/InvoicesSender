import PyPDF2
import os

class PdfAnalyzer:
    """ Pick PDFs with specified sentence.
        This class also detects not sent invoices,
            and invoices delivered to two recipents. 
    """
    def __init__(self, searchedSentence):
        self._searchedSentence = searchedSentence
