import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ctreport_selenium',
    version='1.0.2',
    author='Naveen.S',
    author_email='naveensagayaselvaraj@gmail.com',
    license='MIT',
    description='ctreport for selenium automation will provide simple and creative html file for day to day software testing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url='https://github.com/naveens33/ctreport-selenium',
    download_url='https://github.com/naveens33/ctreport-selenium/archive/0.1.1.tar.gz',
    install_requires=[
        'datetime',
        'shutil'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
