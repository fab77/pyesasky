var widgets = require('@jupyter-widgets/base');
var _ = require('underscore');

//var mytest = require('./api.js');


var ESASkyJSModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(_.result(this, 'widgets.DOMWidgetModel.prototype.defaults'), {
        _model_name : 'ESASkyJSModel',
        _view_name : 'ESASkyJSView',
        _model_module : 'pyesasky',
        _view_module : 'pyesasky',
        _test_msg : 'Ciao ciao',
        _target : ''
    })
});

var ESASkyJSView = widgets.DOMWidgetView.extend({
    
	initialize: function() {
		
		var div = document.createElement("div");
		
//		this.base_url = require('@jupyterlab/coreutils').Pageconfig.getBaseUrl();
		
//		div.innerHTML = "<iframe id='esaskyFrame' width='100%' height='800' style='border: none;' src='http://sky-int.esac.esa.int/index.html'</iframe>";
		div.innerHTML = "<iframe id='esaskyFrame' width='100%' height='800' style='border: none;' src='http://localhost:8888/nbextensions/pyesasky/esasky.html'</iframe>";
		//div.innerHTML = "<iframe width='100%' height='800' style='border: none;' src='" + this.base_url + "pyesasky/esasky.html'</iframe>";
		
		this.el.appendChild(div);
//		ESASkyJSView.__super__.initialize(this, arguments);
		
	},
	
	
	render: function() {    
		console.log("render 0");
    	this.value_changed();
    	console.log("render 1");
    	this.model.on('change:_test_msg', this.value_changed, this);
    	this.model.on('change:_target', this.target_changed, this);
        console.log("render 2");
    },

    value_changed: function() {
		console.log("_test_msg_changed 0");
//		mytest.test(this.model.get("_test_msg"));
		console.log("_test_msg_changed 1");
//		document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.goToTargetName("M51");

//		mytest2.ESASkyAPI.goToTargetName("M51");
	},
    
    target_changed: function() {
    	console.log("Target changed "+this.model.get("_target"));
    	document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.goToTargetName(this.model.get("_target"));
    }
});


module.exports = {
	ESASkyJSModel: ESASkyJSModel,
	ESASkyJSView: ESASkyJSView
};