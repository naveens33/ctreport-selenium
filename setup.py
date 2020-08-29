import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ctreport_selenium',
    version='1.1.4',
    author='Naveen.S',
    author_email='naveensagayaselvaraj@gmail.com',
    license='MIT',
    description='ctreport-selenium is a simple, creative and a customizable report for automation testing using Python. Best suitable for pytest, unit test and nose framework.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url='https://naveens33.github.io/ctreport-selenium/',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
