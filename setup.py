#!/usr/bin/python3
"""Setup
"""
from setuptools import find_packages
from distutils.core import setup

version = "0.5.0dev1"

with open('README.rst') as f:
    long_description = f.read()

setup(name='ofxstatement-iso20022',
      version=version,
      author="Andrey Lebedev",
      author_email="andrey@lebedev.lt",
      url="https://github.com/kedder/ofxstatement-iso20022",
      description=("ISO-20022 plugin for ofxstatement"),
      long_description=long_description,
      license="GPLv3",
      keywords=["ofx", "banking", "statement"],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Natural Language :: English',
          'Topic :: Office/Business :: Financial :: Accounting',
          'Topic :: Utilities',
          'Environment :: Console',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU Affero General Public License v3'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=["ofxstatement", "ofxstatement.plugins"],
      entry_points={
          'ofxstatement':
          ['iso20022 = ofxstatement.plugins.iso20022:Iso2022Plugin']
          },
      install_requires=['ofxstatement'],
      extras_require={"test": ["pytest"]},
      include_package_data=True,
      zip_safe=True
      )
