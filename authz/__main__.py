# -~- coding: utf-8 -~-

from .version import __version__
from .version import __author__
from .version import __licence__

from . import DockerAuthApp

if __name__ == "__main__":
    APP = DockerAuthApp()
    APP.app.run()

