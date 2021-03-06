#!/usr/bin/env python

from setuptools import setup

setup(
    name='mezzanine-openshift',
    version='1.0',
    description='Mezzanine configured for deployment on OpenShift.',
    author='Isaac Bythewood',
    author_email='isaac@bythewood.me',
    url='http://isaacbythewood.com/',
    install_requires=[
        'Django>=1.4.3',
        'mezzanine>=1.4.0',
        'django_compressor==1.2'
    ],
)
