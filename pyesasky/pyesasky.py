import ipywidgets as widgets
from traitlets import Unicode, default, Float
from docutils.nodes import target
from statsmodels.tsa.statespace.tests.test_mlemodel import kwargs


__all__ = ['ESASkyWidget']

#class ESASkyWidget(HasTraits, widgets.DOMWidget):
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
        