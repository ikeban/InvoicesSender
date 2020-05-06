from code.PdfReader import PdfReader
from unittest.mock import MagicMock

def test_can_create_PdfReader():
    pdfReader = PdfReader()
    assert pdfReader._invoiceMap is not None

def test_readed_invoices_map():
    #pdfReader = PdfReader()
    #print("\nInvoice map: " + str(pdfReader.getReadedInvoicesMap()))
    pass
    

def test_real_output():
    #pdfReader = PdfReader()
    #print("\nReaded invoices: " + str(pdfReader._getAllInvoicesNames()))
    pass
