# -*- coding: utf-8 -*-
#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)
import codecs
import sys

from setuptools import setup, find_packages

install_requirements = [
    "python-dateutil",
    "six",
    "convertdate",
    "korean_lunar_calendar",
]

if sys.version_info >= (3, 6):
    install_requirements.append("hijri_converter")

setup(
    name="holidays",
    version="0.10.3",
    author="ryanss",
    author_email="ryanssdev@icloud.com",
    maintainer="dr-prodigy",
    maintainer_email="maurizio.montel@gmail.com",
    url="https://github.com/dr-prodigy/python-holidays",
    packages=find_packages(),
    license="MIT",
    description="Generate and work with holidays in Python",
    long_description=codecs.open("README.rst", encoding="utf-8").read(),
    long_description_content_type="text/x-rst",
    install_requires=install_requirements,
    platforms="any",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Office/Business :: Scheduling",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Localization",
    ],
)
