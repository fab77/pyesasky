
__all__ = ['CatalogueDescriptor']

class CatalogueDescriptor:
    
    _sourceLimit = 9999
    _sourceLimitDescription = ''
    _posTapColumn  = ''
    _polygonRaTapColumn = ''
    _polygonDecTapColumn = ''
    _polygonNameTapColumn = ''
    _orderBy  = ''
    _mission = ''
    _tapTable = ''
    _guiShortName = ''
    _guiLongName = ''
    _histoColor = ''
    _fovLimit = 0
    _archiveURL = ''
    _archiveProductURI = ''
    _tabCount = 0
    _metadata = []


    def __init__(self, name, color, raColumn, decColumn, nameColumn, metadata):
        self._mission = name
        self._guiShortName = name
        self._guiLongName = name

        self._polygonRaTapColumn = raColumn
        self._polygonDecTapColumn = decColumn
        self._polygonNameTapColumn = nameColumn

        self._histoColor = color

        self._metadata = metadata

    def toDict(self):
        
        content = dict(
            mission=self._mission,
            tapTable='',
            countColumn='',
            guiShortName=self._guiShortName,
            guiLongName=self._guiLongName,
            histoColor=self._histoColor,
            countFovLimit=360,
            fovLimit=90.0,
            archiveURL='',
            archiveProductURI='',
            adsPublicationsMaxRows=0,
            tabCount=0,
            sourceLimit=100000,
            sourceLimitDescription='',
            posTapColumn='pos',
            polygonRaTapColumn=self._polygonRaTapColumn,
            polygonDecTapColumn=self._polygonDecTapColumn,
            polygonNameTapColumn=self._polygonNameTapColumn,
            orderBy='',
            metadata=self._metadata
        )
        return content
        


