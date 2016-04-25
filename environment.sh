#!/bin/sh
cd ~
mkdir popoola_ebenezer
cd popoola_ebenezer

VENV=~/popoola_ebenezer/env
export VENV
pyvenv VENV

wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | VENV/bin/python

VENV/bin/easy_install "pyramid==1.6.1"

VENV/bin/easy_install nose webtest deform sqlalchemy pyramid_chameleon pyramid_debugtoolbar waitress pyramid_tm zope.sqlalchemy

VENV/bin/easy_install bs4 requests




