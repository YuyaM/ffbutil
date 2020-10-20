#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ffbutil',
    version='0.7.3.2',
    description='Utility program package for FrontFlow/Blue',
    long_description=long_description,
    url='https://github.com/YuyaM/ffbutil',
    author='YuyaM',
    author_email='',
    license='MIT',
    install_requires=['numpy', 'scipy', 'pandas', 'matplotlib'],
    keywords='ffbutil',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
