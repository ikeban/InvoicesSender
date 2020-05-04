from ExcelParser import ExcelParser

from unittest.mock import MagicMock

def test_can_create_ExcelParser():
    excelParser = ExcelParser()
    assert excelParser.excel is not None
