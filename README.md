# pyesasky

ESASky Jupyter widget

# Installation

For a development installation (requires npm),

$ git clone https://github.com/fab77/pyesasky.git

$ cd pyesasky

$ python setup.py install

$ pip install .

$ jupyter nbextension install --py --sys-prefix pyesasky

$ jupyter nbextension enable --py --sys-prefix pyesasky



Once installed open Jupyter notebook

$ jupyter notebook


from pyesasky.pyesasky import ESASkyWidget

esasky = ESASkyWidget()

esasky



## go to a target by name
esasky.goToTargetName('M51')

## go to RA and Dec
esasky.setGoToRADec('10 0 2', '+10 1 23')
esasky.setGoToRADec('45', '+81.7')

## set the FoV in decimal degrees
esasky.setFoV(1)

## use the Planck color palette for the current HiPS
esasky.setHiPSColorPalette('PLANCK')

## use the Native color palette for the current HiPS
esasky.setHiPSColorPalette('NATIVE')

## User Catalogue overlay

from pyesasky.pyesasky import Catalogue
catalogue = Catalogue('test catalogue', 'equatorial', '#ee2345', 10)
catalogue.addSource('A', '105.69239256', '-8.45235969')
catalogue.addSource('B', '105.70779763', '-8.31350997')
esasky.overlayCatalogue(catalogue)
esasky.setGoToRADec('105.69239256', '-8.45235969')

# Uninstall

$ cd pyesasky

$ pip uninstall pyesasky

$ python setup.py clean

$ npm run clean

$ jupyter nbextension uninstall pyesasky

In case the uninstall will complain about a missing 'rimraf' command, try that first and then rerun the uninstall procedure:

$ npm install webpack-dev-server rimraf webpack -g
