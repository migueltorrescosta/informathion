# -*- coding: utf-8 -*-
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='informathion',
    version='0.1.6',
    description='Framework for Minimizing Opportunity Loss',
    long_description=readme(),
    author='Miguel Torres Costa',
    author_email='miguelptcosta1995@gmail.com',
    maintainer='migueltorrescosta',
    maintainer_email=None,
    url='https://github.com/migueltorrescosta/informathion',
    packages='informathion',
    package_data=package_data,
    install_requires=[
    'matplotlib>=3.4.2,<4.0.0',
    'numpy>=1.20.3,<2.0.0',
    'pandas>=2.1.0,<2.2.0',
    'seaborn>=0.12.2,<0.13.0'
    ],
    python_requires='>=3.9,<4.0',
)
