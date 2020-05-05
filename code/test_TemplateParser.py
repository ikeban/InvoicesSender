from TemplateParser import TemplateParser
from unittest.mock import MagicMock

def test_can_create_TemplateParser():
    templateParser = TemplateParser("", {})
    assert templateParser._templateText is not None
    assert templateParser._keywordsMap is not None
    assert templateParser._filledTemplate is not None

def test_template_is_filled_correctly():
    keywordMap = {"[TITLE]" : "Dear Miky,", "[SIGNATURE]" : "Patrick"}
    templateParser = TemplateParser("[TITLE]\n\nHello!\n[SIGNATURE]", keywordMap)
    assert templateParser.getFilledTemplate() == "Dear Miky,\n\nHello!\nPatrick"
