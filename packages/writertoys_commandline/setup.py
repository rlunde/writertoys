#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='writertoys_commandline',
    version='0.1.0',
    description="WriterToys CommandLine contains the code to support the web app business logic, and command line utilities and tests.",
    long_description=readme + '\n\n' + history,
    author="Ron Lunde",
    author_email='r_lunde@yahoo.com',
    url='https://github.com/rlunde/writertoys_commandline',
    packages=[
        'writertoys_commandline',
    ],
    package_dir={'writertoys_commandline':
                 'writertoys_commandline'},
    entry_points={
        'console_scripts': [
            'writertoys_commandline=writertoys_commandline.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='writertoys_commandline',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
