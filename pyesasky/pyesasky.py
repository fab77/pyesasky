import ipywidgets as widgets
from traitlets import Unicode, default
#from traitlets import HasTraits, observe, validate, TraitError
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
    _test_msg = Unicode('default text').tag(sync=True)
    _target = Unicode('default text').tag(sync=True)
    
    
 #   def __init__(self, **kwargs):
 #       super(ESASkyWidget, self).__init__()
 #       self.observe(self._on_trait_change, type='change')
    
    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='400px', align_self='stretch')

    def goTo(self, target):
        self._target = target 
        