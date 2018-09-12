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

esasky.goTo('M1')


# uninstall

$ cd pyesasky
$ pip uninstall pyesasky
$ python setup.py clean
$ npm run clean
$ jupyter nbextension uninstall pyesasky
