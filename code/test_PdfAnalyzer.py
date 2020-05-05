from code.PdfAnalyzer import PdfAnalyzer
from unittest.mock import MagicMock

def test_can_create_PdfAnalyzer():
    pdfAnalyzer = PdfAnalyzer({})
    assert pdfAnalyzer._pdfNameToContentMap is not None

def test_search_sentence_and_update_stats():
    pdfAnalyzer = PdfAnalyzer({"test1.txt" : "my\ncontent\nCompanyNorth",
                               "test2.txt" : "my\ncontent\nCompanyNorth Basinn",
                               "test3.txt" : "my\ncontent\nPatrick Smith"})
    serachResult = pdfAnalyzer.searchSentenceAndUpdateStats("CompanyNorth")
    assert serachResult == ["test1.txt", "test2.txt"]
    serachResult2 = pdfAnalyzer.searchSentenceAndUpdateStats("Basinn")
    assert serachResult2 == ["test2.txt"]
    pdfAnalyzer.dropStatistics()
