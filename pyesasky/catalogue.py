
__all__ = ['Catalogue']


class Catalogue:
    
    _catalogueName = ''
    _cooframe = 'equatorial'
    _color = '#ee2345'
    _lineWidth = 10
    _sources = []
    
    
    
    def __init__(self, catalogueName, cooframe, color, lineWidth):
        _catalogueName = catalogueName
        _cooframe = cooframe
        _color = color
        _lineWidth = lineWidth
        
    def addSource(self, name, ra, dec):
#        currSource = {}
#        currSource['data'] = {}
#        currSource['name'] = name.decode('utf-8')
#        currSource['ra'] = ra
#        currSource['dec'] = dec
#        currSource['data']['sourceType'] = 'Catalogue'
        currSource = dict(
                          name=name.decode('utf-8'),
                          ra=ra,
                          dec=dec
                          )
        self._sources.append(currSource)
        
    def toDict(self):
        
        content=dict(
            catalogue= dict(
                catalogueName=self._catalogueName,
                cooframe=self._cooframe,
                color=self._color,
                lineWidth=self._lineWidth,
                sources=self._sources
            )
        )
        return content
    
        