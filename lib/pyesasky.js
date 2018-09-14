var widgets = require('@jupyter-widgets/base');
var _ = require('underscore');

var ESASkyJSModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(_.result(this, 'widgets.DOMWidgetModel.prototype.defaults'), {
    	_model_name : 'ESASkyJSModel',
        _view_name : 'ESASkyJSView',
        _model_module : 'pyesasky',
        _view_module : 'pyesasky',
        _targetname : '',
        _fovDeg : 30,
        _colorPalette: 'NATIVE'
    })
});

var ESASkyJSView = widgets.DOMWidgetView.extend({
    
	initialize: function() {
		
		var div = document.createElement("div");
		
		//this.base_url = require('@jupyterlab/coreutils').Pageconfig.getBaseUrl();
		div.innerHTML = "<iframe id='esaskyFrame' width='100%' height='800' style='border: none;' src='http://localhost:8888/nbextensions/pyesasky/esasky.html'</iframe>";
		//div.innerHTML = "<iframe width='100%' height='800' style='border: none;' src='" + this.base_url + "pyesasky/esasky.html'</iframe>";
				
		this.el.appendChild(div);
		
	},
	
	
	render: function() {    
		
		this.model.on('change:_targetname', this.target_changed, this);
		this.model.on('change:_fovDeg', this.fovDeg_changed, this);
		this.model.on('change:_colorPalette', this.colorPalette_changed, this);
		
		this.model.on('msg:custom', this.handle_custom_message, this);

    },

    target_changed: function() {
    	console.log("Targetname changed "+this.model.get("_targetname"));
    	document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.goToTargetName(this.model.get("_targetname"));
    },
    
    fovDeg_changed: function() {
    	console.log("FoV changed "+this.model.get("_fovDeg"));
    	document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.setFoV(this.model.get("_fovDeg"));
    },
    
    colorPalette_changed: function() {
    	console.log("ColorPalette changed "+this.model.get("_colorPalette"));
    	document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.setHiPSColorPalette(this.model.get("_colorPalette"));
    },
    
    handle_custom_message: function(msg) {
    	console.log('event captured!');
    	console.log(msg);
    	switch(msg['event']){
    		case 'goToRADec':
    			console.log('goToRADec event captured!');
    			return document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.goTo(msg['ra'],msg['dec']);
    			break;
    		
    		case 'overlayCatalogue':
    			console.log('overlayCatalogue event captured!');
    			console.log(msg);
    			var catJSON = JSON.stringify(msg['content']);
    			alert(catJSON);
    			return document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.overlayCatalogue(catJSON);
    			
    			
    		default:
    			console.log('No event associated');
    	}
    	
    	
    }
    
});

module.exports = {
	ESASkyJSModel: ESASkyJSModel,
	ESASkyJSView: ESASkyJSView
};