#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["aiohttp", "python-dateutil"]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
    "aiounittest",
    "aioresponses",
]

setup(
    author="J. Nick Koston",
    author_email="nick@koston.org",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Python API for Griddy Wholesale Electricity",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="griddypower",
    name="griddypower",
    packages=find_packages(include=["griddypower", "griddypower.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/bdraco/griddypower",
    version="0.1.0",
    zip_safe=False,
)
