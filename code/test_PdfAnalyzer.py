from code.PdfAnalyzer import PdfAnalyzer
from unittest.mock import MagicMock

def test_can_create_PdfAnalyzer():
    pdfAnalyzer = PdfAnalyzer("Nothing")
    assert pdfAnalyzer._searchedSentence is not None
