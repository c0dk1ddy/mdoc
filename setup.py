from setuptools import setup, find_packages
from json import load as _l
getJ = lambda f : _l(open(f))

setup_by_json = lambda f : setup(packages=find_packages(exclude=[]), **getJ(f))

setup_by_json('setup.json')