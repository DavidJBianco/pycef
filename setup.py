#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pycef',
      version='1.02',
      description='A very simple CEF parser.',
      long_description=long_description,
      url='https://github.com/DavidJBianco/pycef',
      author='David J. Bianco',
      author_email='davidjbianco@gmail.com',
      license='MIT',
      keywords=['cef','parser','CEF'],
      packages=['pycef'],
      tests_require=['future','pytest'],
      setup_requires=['pytest-runner'],
      install_requires=['future'],
      zip_safe=True,
      classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License"
      ]
)
