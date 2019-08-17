#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import autoit
import os

setup(
    name='pyautoit-64',
    version="1.0.0",
    packages=['autoit'],
    package_data={'': ['lib\\*.dll']},
    url='https://github.com/xuepl/pyautoit-64.git',
    license='MIT',
    author='xuepl',
    author_email='xuepl@guoyasoft.com',
    description='Python binding for AutoItX3.dll 支持64位dll',
    platforms="python"
)

