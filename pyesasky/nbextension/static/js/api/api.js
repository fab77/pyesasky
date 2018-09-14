var ESASkyAPI = null;

function ESASkyAPIConstructor() {

	this.goTo = function(ra, dec) {
		this.goToAPI(ra, dec);
	};

	this.goToWithParams = function(ra, dec, fovDegrees, showTargetPointer, cooFrame) {
        this.goToWithParamsAPI(ra, dec, fovDegrees, showTargetPointer, cooFrame);
    };

	this.goToTargetName = function(targetName) {
        this.goToTargetNameAPI(targetName);
    };

    this.goToTargetNameWithFoV = function(targetName, fovDeg) {
        this.goToTargetNameWithFoVAPI(targetName, fovDeg);
    };

	this.setFoV = function(fovDegrees) {
		this.setFoVAPI(fovDegrees);
	};

	this.setHiPSWithParams = function(surveyId, surveyName, surveyRootUrl,
			surveyFrame, maximumNorder, imgFormat) {
		this.setHiPSWithParamsAPI(surveyId, surveyName, surveyRootUrl,
				surveyFrame, maximumNorder, imgFormat);
	};

	this.setHiPSColorPalette = function(colorPalette) {
		this.setHiPSColorPaletteAPI(colorPalette);
	};

	this.overlayCatalogue = function(catalogueJSON){
		console.log(catalogueJSON);
		this.overlayCatalogueAPI(catalogueJSON);
	};

//	this.addEventListener("sourceSelected",function(e) {
//                console.log(e.detail);
//    });

}

function JavaApiReady() {
	ESASkyAPI = new ESASkyAPIConstructor();
}

module.exports.ESASkyAPI = ESASkyAPI;
// CALL FROM PYTHON EXAMPLE
// ESASkyAPI.goTo("10","+26");
//
// ESASkyAPI.setFoV(40);
//
// ESASkyAPI.setHiPSWithParams("Planck LFI 030 GHz Pol smoothed", "Planck LFI 030 GHz Pol smoothed", "http://skies.esac.esa.int/pla/LFI_SkyMap_030_1024_R3_00_full_smooth_HiPS/", "Galactic", 3, "png");
//
// ESASkyAPI.setHiPSColorPalette("PLANCK");
//
// ESASkyAPI.goToTargetName("M51");
//
// ESASkyAPI.goToWithParams("10", "-25", 10.3, true, "Equatorial"); // some problem with Galactic
//
// ESASkyAPI.goToTargetNameWithFoV("M1", 10);
//
//
//var catalogueJSON = "{
//	"catalogue": {
//		"catalogueName": "bla bla bla",
//		"cooframe": "equatorial",
//		"color":"#ee2345",
//		"lineWidth":10,
//		"coords": [
//			{
//				"name": "A",
//				"ra": "105.69239256",
//				"dec": "-8.45235969"
//			},{
//				"name": "B",
//				"ra": "105.70779763",
//				"dec": "-8.31350997"
//			},{
//				"name": "C",
//				"ra": "105.74242906",
//				"dec": "-8.34776709"
//			}
//		]
//	}
//}";
// ESASkyAPI.overlayCatalogue("{\"catalogue\":{\"catalogueName\": \"bla bla bla\",\"cooframe\": \"equatorial\",\"color\":\"#ee2345\",\"lineWidth\":10,\"sources\": [{\"name\": \"A\",\"ra\": \"105.69239256\",\"dec\": \"-8.45235969\"},{\"name\": \"B\",\"ra\": \"105.70779763\",\"dec\": \"-8.31350997\"},{\"name\": \"C\",\"ra\": \"105.74242906\",\"dec\": \"-8.34776709\"}]}}");
