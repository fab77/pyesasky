
__all__ = ['Catalogue']


class Catalogue:
    
    _catalogueName = ''
    _cooframe = 'J2000'
    _color = '#aa2345'
    _lineWidth = 10
    _sources = []
    
    
    
    def __init__(self, catalogueName, cooframe, color, lineWidth):
        self._catalogueName = catalogueName
        
        if (cooframe == 'J2000' or cooframe == 'Galactic'): 
            self._cooframe = cooframe
        else:
            print('coordinates frame ' + cooframe + ' not recognized. Possible options are J2000 and Galactic. Applied J2000 by default.')

        if color:
            self._color = color
        
        self._lineWidth = lineWidth
        
    def addSource(self, name, ra, dec):
        currSource = {}
        currSource['data'] = {}
        currSource['name'] = str(name).decode('utf-8')
        currSource['ra'] = ra
        currSource['dec'] = dec
        currSource['data']['sourceType'] = 'Catalogue'
        self._sources.append(currSource)
        
    def toDict(self):
        
        content = dict(
            catalogue=dict(
                catalogueName=self._catalogueName,
                cooframe=self._cooframe,
                color=self._color,
                lineWidth=self._lineWidth,
                sources=self._sources
            )
        )
        return content
    
        
