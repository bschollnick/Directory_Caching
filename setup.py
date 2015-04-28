#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup, find_packages
except:
    from disutils.core import setup, find_packages

__title__ = 'directory_caching'
__version__ = '1.10.2'
__author__ = 'Benjamin Schollnick'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Benjamin Schollnick'

dependencies = ['natsort', 'scandir']

classifiers = """\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: OS Independent
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft :: Windows
Operating System :: Unix
Programming Language :: Python
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
"""

# #
# #   Modelled after requests - https://github.com/kennethreitz/requests/blob/master/setup.py
# #
# setup(
#     name='directory_caching',
#     version=__version__,
#     description = doclines[0],
#     long_description = "\n".join(doclines[2:]),
#     author=__author__,
#     author_email='benjamin@schollnick.net',
#     url='https://github.com/bschollnick/Directory_Caching/tree/master',
#     license="MIT",
#     maintainer='Benjamin Schollnick',
#     maintainer_email='benjamin@schollnick.net',
#     packages=find_packages(),
#     package_dir={'directory_caching': 'directory_caching'},
#     include_package_data=True,
# #    platforms=["Any"],
#     download_url = 'https://github.com/bschollnick/Directory_Caching/tarball/1.05',
#     install_requires=dependencies,
#     keywords = ['caching', 'files', 'directories', 'scandir', 'naturalsort'],
#     classifiers=filter(None, classifiers.split("\n")),
# )

#
# https://github.com/michaelhelmick/lassie/blob/master/setup.py
#
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'directory_caching',
]

setup(
    name='directory_caching',
    version=__version__,
    install_requires=[
        'requests==2.6.0',
        'scandir==0.9',
        'natsort==3.5.2'
    ],
    author='Benjamin Schollnick',
    author_email='benjamin@schollnick.net',
    license=open('LICENSE').read(),
    url='https://github.com/bschollnick/Directory_Caching/tree/master',
    keywords='caching files directories scandir naturalsort',
    description='Caching system for Directory and File Listings',
#    long_description=open('README.rst').read() + '\n\n' +
#                     open('HISTORY.rst').read(),
    include_package_data=True,
    packages=packages,
    classifiers=filter(None, classifiers.split("\n"))
)