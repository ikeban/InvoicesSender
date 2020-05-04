import openpyxl

class ExcelParser:
    """ Reads all needed data from excel file """
    def __init__(self, excelFileName='../InvoiceSenderControl.xlsx'):
        self.excel = openpyxl.load_workbook(excelFileName)
