"""Directory Caching - A Caching library for Directories & Files

The Directory Caching library caches and manages directory and file listings data.
The library is being developed for the (Web) Gallery software.
"""

classifiers = """\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Database
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: OS Independent
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft :: Windows
Operating System :: Unix
Programming Language :: Python
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
"""
try:
    from setuptools import setup, find_packages
except:
    from disutils.core import setup, find_packages

__title__ = 'Directory_Caching'
__version__ = '1.0.6b1'
__author__ = 'Benjamin Schollnick'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Benjamin Schollnick'

dependencies = ['natsort', 'scandir']

doclines = __doc__.split("\n")

#
#   Modelled after requests - https://github.com/kennethreitz/requests/blob/master/setup.py
#
setup(
    name='Directory_Caching',
    version='1.0.10',
    description = doclines[0],
    long_description = "\n".join(doclines[2:]),
    author='Benjamin Schollnick',
    author_email='benjamin@schollnick.net',
    url='https://github.com/bschollnick/Directory_Caching',
    license="MIT",
    maintainer='Benjamin Schollnick',
    maintainer_email='benjamin@schollnick.net',
    packages=find_packages(),
#    py_module=['Directory_Caching'],
#    package_dir={'Directory_Caching': ''},
    include_package_data=True,
#    platforms=["Any"],
    download_url = 'https://github.com/bschollnick/Directory_Caching/tarball/1.05',
    install_requires=dependencies,
    keywords = ['caching', 'files', 'directories', 'scandir', 'naturalsort'],
    classifiers=filter(None, classifiers.split("\n")),
)
