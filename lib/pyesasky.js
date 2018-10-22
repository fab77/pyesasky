var widgets = require('@jupyter-widgets/base');
var _ = require('underscore');

var ESASkyJSModel = widgets.DOMWidgetModel.extend({
	defaults: _.extend(_.result(this, 'widgets.DOMWidgetModel.prototype.defaults'), {
		_model_name: 'ESASkyJSModel',
		_view_name: 'ESASkyJSView',
		_model_module: 'pyesasky',
		_view_module: 'pyesasky',
		_targetname: '',
		_fovDeg: 30,
		_colorPalette: 'NATIVE'
	})
});

var ESASkyJSView = widgets.DOMWidgetView.extend({

	initialize: function () {
	},


	render: function () {
		var div = document.createElement("div");
		this.base_url = require('@jupyterlab/coreutils').PageConfig.getBaseUrl();
		this.base_url = require('@jupyterlab/coreutils').PageConfig.getBaseUrl();

		div.innerHTML = "<iframe id='esaskyFrame' width='100%' height='800' style='border: none;' src='" + this.base_url + "nbextensions/pyesasky/esasky.html?log_level=DEBUG'</iframe>";
		this.el.appendChild(div);

		this.model.on('change:_targetname', this.target_changed, this);
		this.model.on('change:_fovDeg', this.fovDeg_changed, this);
		this.model.on('change:_colorPalette', this.colorPalette_changed, this);

		this.model.on('msg:custom', this.handle_custom_message, this);

	},


	target_changed: function () {
		console.log("Targetname changed " + this.model.get("_targetname"));
		document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.goToTargetName(this.model.get("_targetname"));
	},

	fovDeg_changed: function () {
		console.log("FoV changed " + this.model.get("_fovDeg"));
		document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.setFoV(this.model.get("_fovDeg"));
	},

	colorPalette_changed: function () {
		console.log("ColorPalette changed " + this.model.get("_colorPalette"));
		document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.setHiPSColorPalette(this.model.get("_colorPalette"));
	},

	handle_custom_message: function (msg) {
		console.log('Inside pyesasky.js');
		console.log('event captured!');
		console.log(msg);
		switch (msg['event']) {
			case 'goToRADec':
				console.log('goToRADec event captured!');
				return document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.goTo(msg['ra'], msg['dec']);
				break;

			case 'overlayCatalogue':
				console.log('overlayCatalogue event captured!');
				console.log(msg);
				var catJSON = JSON.stringify(msg['content']);
				return document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.overlayCatalogue(catJSON);


			case 'changeHiPS':
				console.log('changeHiPS event captured!');
				console.log(msg);
				return document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.setHiPSWithParams(msg['id'], msg['name'], msg['url'], msg['cooframe'], msg['maxnorder'], msg['imgformat']);

			case 'clearCatalogue':
				console.log('clear catalgue event captured!');
				console.log(msg);
				return document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.clearCatalogue(msg['content']);

			case 'removeCatalogue':
				console.log('remove catalgue event captured!');
				console.log(msg);
				return document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.removeCatalogue(msg['content']);

			case 'overlayFootprints':
				console.log('overlayFootprints event captured!');
				console.log(msg);
				var footpeintSetJSON = JSON.stringify(msg['content']);
				return document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.overlayFootprints(footpeintSetJSON);

			case 'clearFootprintsOverlay':
				console.log('clearFootprintsOverlay event captured!');
				console.log(msg);
				return document.getElementById('esaskyFrame').contentWindow.ESASkyAPI.removeAllFootprintsFromOverlay(msg['content']);
				

			case 'deleteFootprintsOverlay':
				console.log('deleteFootprintsOverlay event captured!');
				console.log(msg);

			default:
				console.log('No event associated');
		}


	}

});

module.exports = {
	ESASkyJSModel: ESASkyJSModel,
	ESASkyJSView: ESASkyJSView
};
