#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Setup for project module
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

try:
    from pip.req import parse_requirements
    from pip.download import PipSession

    def requirements(filename='requirements.txt'):
        """
        @returns list parsed required packages
        """
        required = parse_requirements(filename, session=PipSession())
        return [str(ir.req) for ir in required]
except ImportError:

    def requirements(filename='requirements.txt'):
        """
        @returns list parsed required packages
        """
        with open(filename, 'r') as filehandler:
            required = filehandler.read().splitlines()

        return required

from os import path

def read(*paths):
    """ read file contents """
    with open(path.join(*paths), 'r') as filename:
        return filename.read()

exec(read("authz/version.py"))

setup(
    name=__pkgname__,
    version=__version__,
    author_email=__author_email__,
    author="Everett Toews",
    maintainer="Dwight Spencer",
    maintainer_email="support@dapla.net",
    url="https://github.com/denzuko/docker-authz-plugin/new/master",
    download_url="https://github.com/denzuko/docker-authz-plugin/releases",
    description="restful api for docker authentication plugin",
    long_description=(read('README.md')),
    license="MIT",
    keywords="docker restful api authentication plugin",
    platforms=['docker', 'linux'],
    include_package_data=True,
    install_requires=requirements(),
    packages=find_packages(),
    scripts=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Telecommunications Industry",
        "Intended Audience :: System Administrators",
        "Framework :: Flask",
        "Framework :: Eve",
        "Environment : OpenStack",
        "Environment : No Input/Output (Daemon)",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=False,
)
