#!/bin/bash




# uninstall
echo "uninstalling current version"
pip uninstall pyesasky
python setup.py clean
npm run clean
jupyter nbextension uninstall pyesasky

sleep 2

# install

echo "installing"
python setup.py install
pip install .
jupyter nbextension install --py --sys-prefix pyesasky
jupyter nbextension enable --py --sys-prefix pyesasky
