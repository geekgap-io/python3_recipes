# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python3_recipes',
    version='1.0.0',
    description='A collection of practical recipes to master Python3 in depth.',
    long_description=readme,
    author='Junior Teudjio Mbativou',
    author_email='jun.teudjio@gmail.com',
    url='https://github.com/junteudjio/python3_recipes',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

