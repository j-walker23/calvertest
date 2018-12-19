#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
  name='calvertest',
  description='calvertest',
  long_description="calvertest",
  author='john',
  author_email='john@chaosdevs.com',
  zip_safe=False,
  packages=find_packages(),
  include_package_data=True,
  python_requires='~=3.7',
  install_requires=[
  ],
  entry_points='''
    [console_scripts]
    cvt=calvertest:cli
  '''
)
