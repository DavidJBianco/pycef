#!/usr/bin/env python

from setuptools import setup

setup(name='pycef',
      version='1.0',
      description='A very simple CEF parser for Python 2/3.',
      url='https://github.com/DavidJBianco/pycef',
      author='David J. Bianco',
      author_email='davidjbianco@gmail.com',
      packages=['pycef'],
      tests_require=['future', 'pytest'],
      setup_requires=['pytest-runner'],
      install_requires=['future'],
      zip_safe=True,
      classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 2.7"
      ]
)
