
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
        currSource = dict(
                          name=name,
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
    
        