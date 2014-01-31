import sys
from setuptools import setup, find_packages

py26_dependency = []
if sys.version_info <= (2, 6):
    py26_dependency = ["argparse >= 1.2.1"]

setup(
    name='compleat',
    version='0.0.1',
    description="Fetch autocomplete suggestions from Google Search. Use responsibly. Not affiliated with Google.",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3'
    ],
    keywords='autocomplete google search',
    author='Jeremy Singer-Vine',
    author_email='jsvine@gmail.com',
    url='http://github.com/jsvine/compleat/',
    license='MIT',
    packages=find_packages(exclude=['test',]),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        "requests >= 2.2.1",
        "unicodecsv >= 0.9.4"
    ] + py26_dependency,
    extras_require={
        "dataset": [ "dataset" ]    
    },
    tests_require=[],
    test_suite='test',
    entry_points={
        'console_scripts': [
            'compleat = compleat.cli:main',
        ]
    }
)
