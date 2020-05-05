
class TemplateParser:
    """ Fill Keywords in template """
    def __init__(self, templateText, keywordsMap):
        self._templateText = templateText
        self._keywordsMap = keywordsMap
        self._filledTemplate = ""
        self._fillTemplateWithKeywords()
        
    def getFilledTemplate(self):
        return self._filledTemplate

    def _fillTemplateWithKeywords(self):
        self._filledTemplate = self._templateText
        for keyword, keywordValue in self._keywordsMap.items():
            self._filledTemplate = self._filledTemplate.replace(keyword, keywordValue)
