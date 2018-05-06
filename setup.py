#!/usr/bin/env python

try:
    import setuptools
    from setuptools import setup, find_packages
except ImportError:
    import sys
    print("Please install setuptools.")
    sys.exit(1)

f = open('README.rst')
__doc__ = f.read()
f.close()

VERSION = "1.0.7"

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
]
setup(
    name='Simple-AES-Cipher',
    version=VERSION,
    description='Pycrypto based Simple And Easy Cipher on AES',
    long_description=__doc__,
    author='teitei-tk',
    author_email='teitei.tk@gmail.com',
    url='https://github.com/teitei-tk/Simple-AES-Cipher',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    classifiers=classifiers,
    install_requires=open('requirements.txt').read().splitlines(),
    keywords=['cipher', 'aes'],
    download_url='https://github.com/teitei-tk/Simple-AES-Cipher/archive/master.tar.gz'
)
