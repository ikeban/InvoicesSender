from code.ExcelReader import ExcelReader
from unittest.mock import MagicMock

def test_can_create_ExcelReader():
    excelParser = ExcelReader()
    assert excelParser._sheet is not None

    data = excelParser.getData()
    assert data is not None

    print("\ndata is" + str(data))
