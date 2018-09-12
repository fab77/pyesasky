from ._version import version_info, __version__
from .jupyter_server import load_jupyter_server_extension

# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [{'section': 'notebook',
            # the path is relative to the `pyesasky` directory
            'src': 'nbextension/static',
            # directory in the `nbextension/` namespace
            'dest': 'pyesasky',
            # _also_ in the `nbextension/` namespace
            'require': 'pyesasky/extension'}]


def _jupyter_server_extension_paths():
    return [{"module": "pyesasky"}]