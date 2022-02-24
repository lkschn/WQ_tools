from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'somepackage', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='WQ_tools',
    version=version['__version__'],
    description=('Scripts, functions and tools to deal with the water quality part of dfm..'),
    long_description=long_description,
    author='Lisa Schneider',
    author_email='lisa.schneider@deltares.nl',
    license='MIT',
    packages=['WQ_tools'],
    install_requires=['matplotlib>=3.0','datetime>=1.8.1'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    )