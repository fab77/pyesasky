import ipywidgets as widgets
from traitlets import Unicode, default, Float
#from docutils.nodes import target
#from statsmodels.tsa.statespace.tests.test_mlemodel import kwargs
from .catalogue import Catalogue


__all__ = ['ESASkyWidget']


    
class ESASkyWidget(widgets.DOMWidget):

    _view_name = Unicode('ESASkyJSView').tag(sync=True)
    _model_name = Unicode('ESASkyJSModel').tag(sync=True)
    _view_module = Unicode('pyesasky').tag(sync=True)
    _model_module = Unicode('pyesasky').tag(sync=True)
    _view_module_version = Unicode('0.1.0').tag(sync=True)
    _model_module_version = Unicode('0.1.0').tag(sync=True)
    
    _targetname = Unicode('Mkr432').tag(sync=True)
    _fovDeg = Float(60).tag(sync=True)
    _colorPalette = Unicode('NATIVE').tag(sync=True)
    
    
    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='400px', align_self='stretch')

    def setGoToRADec(self, ra, dec):
        content = dict(
                       event='goToRADec',
                       ra=ra,
                       dec=dec
                )
        self.send(content)

    def goToTargetName(self, targetname):
        self._targetname = targetname 
        
    def setFoV(self, fovDeg):
        self._fovDeg = fovDeg
        
    def setHiPSColorPalette(self, colorPalette):
        self._colorPalette = colorPalette
        
    def overlayCatalogue(self, catalogue):
        
        content = dict(
                       event='overlayCatalogue',
                       content=catalogue.toDict()
                       )
        self.send(content)
    
    
    def overlayCatalogueFromAstropyTable(self, catalogueName, table, raColName, decColName, mainIdColName):
        
        raColNameUserInput = True
        decColNameUserInput = True
        mainIdColNameUserInput = True
        
        if not raColName:
            raColName = ''
            raColNameUserInput = False
        
        if not decColName:
            decColName = ''
            decColNameUserInput = False
            
        if not mainIdColName:
            mainIdColName = ''
            mainIdColNameUserInput = False
        
        i = 0
        
        if (not raColNameUserInput and not decColNameUserInput and not mainIdColNameUserInput):
             
            while i < len(table.colnames):
                
                colName = table.colnames[i]
                if len(table[colName].meta) > 0:
                    metaType = table[colName].meta['ucd']
                    print('-----------')
                    print(colName)
                    print(metaType)
                    if ('pos.eq.ra' in metaType and not raColNameUserInput):
                        raColName = colName
                    elif ('pos.eq.dec' in metaType and not decColNameUserInput):
                        decColName = colName
                    elif ('meta.main' in metaType and not mainIdColNameUserInput):
                        mainIdColName = colName 
                i += 1
                
        print('#############')
        print('raColName '+raColName)
        print('decColName '+decColName)
        print('mainIdColName '+mainIdColName)
        
        
        
        gaiaCatalogue = Catalogue(catalogueName, 'equatorial', '#aa2345', 10)
        
        j = 0
        while j < len(table):
            gaiaCatalogue.addSource(table[j][mainIdColName], table[j][raColName], table[j][decColName])
            j += 1
        
        self.overlayCatalogue(gaiaCatalogue)

        
        