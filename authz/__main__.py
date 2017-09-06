# -~- coding: utf-8 -~-
from . import DockerAuthApp

if __name__ == "__main__":
    APP = DockerAuthApp()
    APP.app.run()

