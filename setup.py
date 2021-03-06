import os
from setuptools import setup, Extension
from agibuild.settings import VERSION


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

os.environ['CC'] = 'g++'


module_mpkg = Extension('_support',
                    sources = ['mpkg/support.i'],
                    swig_opts=['-c++'],
                    libraries=['mpkgsupport'])

setup(
    name = "agibuild",
    version = VERSION,
    author = "Sir Anthony",
    author_email = "anthony@adsorbtion.org",
    description = ("AgiliaLinux package builder"),
    license = "MIT",
    keywords = "agilia package",
    url = "",
    packages=['agibuild',],
    ext_package = 'mpkg',
    ext_modules = [module_mpkg],
    py_modules = ['mpkg.support'],
    long_description = read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
    ],
)

