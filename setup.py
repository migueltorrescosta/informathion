# -*- coding: utf-8 -*-
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='informathion',
    version='0.1.6',
    description='Measurements for Expected Opportunity Loss',
    long_description='This package aims to provide a framework for measuring future expected opportunity losses',
    author='migueltorrescosta',
    author_email='miguelptcosta1995@gmail.com',
    maintainer='migueltorrescosta',
    maintainer_email=None,
    url=None,
    packages='informathion',
    package_data=package_data,
    install_requires=[
    'matplotlib>=3.4.2,<4.0.0',
    'numpy>=1.20.3,<2.0.0',
    'pandas>=1.2.4,<2.0.0',
    'seaborn>=0.11.1,<0.12.0'
    ],
    python_requires='>=3.9,<4.0',
)
