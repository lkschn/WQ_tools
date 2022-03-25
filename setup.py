# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="WQ_tools",
    version="0.1.0",
    packages=['WQ_tools'],
    install_requires=['matplotlib>=3.0'],
    zip_safe=False,
    author="Lisa Schneider",
    author_email="lisa.schneider@deltares.nl",
    description=(
        "This package provides the tools for the WQ part fo DFM"
    ),
    license="MIT",
)
