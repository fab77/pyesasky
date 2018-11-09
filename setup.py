from __future__ import print_function

import os
from glob import glob
from os.path import join as pjoin 

from setupbase import (
    create_cmdclass, install_npm, ensure_targets,
    find_packages,  combine_commands, ensure_python, 
    get_version, HERE
)

from setuptools import setup

name = 'pyesasky'

# Ensure a valid python version
ensure_python('>=2.7')

# Get our version
version = get_version(pjoin(name, '_version.py'))

nb_path = pjoin(HERE, name, 'nbextension', 'static')
lab_path = pjoin(HERE, name, 'labextension') 

# Representative files that should exist after a successful build
jstargets = [
    pjoin(nb_path, 'index.js'),
    pjoin(HERE, 'lib', 'plugin.js'),
]

package_data_spec = {
    'pyesasky': [
        'nbextension/static/*.*js*',
        'nbextension/static/*.html',
        'labextension/*.tgz'
    ]
}

data_files_spec = [
    ('share/jupyter/nbextensions/pyesasky', nb_path, '*.js*'),
    ('share/jupyter/nbextensions/pyesasky', nb_path, '*.html'),
    
    ('share/jupyter/nbextensions/pyesasky/js', pjoin(nb_path, 'js'), '*.js*'),
    
    ('share/jupyter/nbextensions/pyesasky/js/jquery', pjoin(nb_path, 'js', 'jquery'), '*.js*'),
    ('share/jupyter/nbextensions/pyesasky/js/highcharts', pjoin(nb_path, 'js', 'highcharts'), '*.js*'),
    ('share/jupyter/nbextensions/pyesasky/js/resizeEvents', pjoin(nb_path, 'js', 'resizeEvents'), '*.js*'),
    ('share/jupyter/nbextensions/pyesasky/js/colorpicker', pjoin(nb_path, 'js', 'colorpicker'), '*.js*'),
    ('share/jupyter/nbextensions/pyesasky/js/sliderSelector', pjoin(nb_path, 'js', 'sliderSelector'), '*.js*'),
    ('share/jupyter/nbextensions/pyesasky/js/datepicker', pjoin(nb_path, 'js', 'datepicker'), '*.js*'),
    ('share/jupyter/nbextensions/pyesasky/js/api', pjoin(nb_path, 'js', 'api'), '*.js*'),
    ('share/jupyter/nbextensions/pyesasky/js/esaskyweb_V3_0', pjoin(nb_path, 'js', 'esaskyweb_V3_0'), '*.js*'),
    
    ('share/jupyter/nbextensions/pyesasky/images', pjoin(nb_path, 'images'), '*.gif*'),
    ('share/jupyter/nbextensions/pyesasky/images', pjoin(nb_path, 'images'), '*.png*'),
    ('share/jupyter/nbextensions/pyesasky/images', pjoin(nb_path, 'images'), '*.ico*'),
    
    ('share/jupyter/nbextensions/pyesasky/internationalization', pjoin(nb_path, 'internationalization'), '*.xml*'),
    
    ('share/jupyter/nbextensions/pyesasky/css', pjoin(nb_path, 'css'), '*.css*'),
    ('share/jupyter/nbextensions/pyesasky/js/esaskyweb_V3_0/gwt/aladinlite', pjoin(nb_path, 'js', 'esaskyweb_V3_0','gwt','aladinlite'), '*.css*'),
    ('share/jupyter/nbextensions/pyesasky/js/esaskyweb_V3_0/gwt/dark', pjoin(nb_path, 'js', 'esaskyweb_V3_0','gwt','dark'), '*.css*'),
    ('share/jupyter/nbextensions/pyesasky/js/esaskyweb_V3_0/gwt/dark/images', pjoin(nb_path, 'js', 'esaskyweb_V3_0','gwt','dark','images'), '*.gif*'),
    ('share/jupyter/nbextensions/pyesasky/js/esaskyweb_V3_0/gwt/dark/images', pjoin(nb_path, 'js', 'esaskyweb_V3_0','gwt','dark','images'), '*.png*'),
    ('share/jupyter/nbextensions/pyesasky/js/esaskyweb_V3_0/gwt/dark/images', pjoin(nb_path, 'js', 'esaskyweb_V3_0','gwt','dark','images'), '*.jpg*'),
    
    
    ('share/jupyter/lab/extensions', lab_path, '*.tgz'),
    ('etc/jupyter/nbconfig/notebook.d' , os.path.join(HERE, 'jupyter.d', 'notebook.d'), 'pyesaky.json'),
    ('etc/jupyter/jupyter_notebook_config.d' , os.path.join(HERE, 'jupyter.d', 'jupyter_notebook_config.d'), 'pyesaky.json')]


cmdclass = create_cmdclass('jsdeps', package_data_spec=package_data_spec,
    data_files_spec=data_files_spec)
cmdclass['jsdeps'] = combine_commands(
    install_npm(HERE, build_cmd='build:all'),
    ensure_targets(jstargets),
)


setup_args = dict(
    name                    = name,
    description             = 'ESASky Python wrapper',
    version                 = version,  
    scripts                 = glob(pjoin('scripts', '*')),
    cmdclass                = cmdclass,
    packages                = find_packages(),
    author                  = 'Fabrizio Giordano from ESDC (ESA/ESAC)',
    author_email            = 'fabriziogiordano77@gmail.com',
    url                     = 'https://github.com/fab77/pyesasky',
    license                 = 'TBD',
    platforms               = 'Linux, Mac OS X, Windows',
    keywords                = ['ipython','jupyter','widgets'],
    classifiers             = [
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    include_package_data    = True,
    install_requires        = [
        'numpy>=1.9',
        'matplotlib>1.5',
        'astropy>=1.0',
        'requests',
        'beautifulsoup4',
        'python-dateutil',
        'lxml',
        'ipywidgets>=7.0.0',
        'ipyevents',
        'traitlets',
        'qtpy',
        'flask',
        'flask-cors',
        'six'
    ],    
    extras_require = {
        'test': [
            'pytest',
            'pytest-cov',
            'nbval',
        ],
        'examples': [
            # Any requirements for the examples to run
        ],
        'docs': [
            'sphinx>=1.5',
            'recommonmark',
            'sphinx_rtd_theme',
            'nbsphinx>=0.2.13',
            'jupyter_sphinx',
            'nbsphinx-link',
            'pytest_check_links',
            'pypandoc',
        ],
    },
    entry_points = {
    },
)

if __name__ == '__main__':
    setup(**setup_args)
