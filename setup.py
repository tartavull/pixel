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
    name='pixel',
    version='0.4.0',
    description="pixel",
    long_description=readme + '\n\n' + history,
    author="Ignacio Tartavull",
    author_email='tartavull@gmail.com',
    url='https://github.com/tartavull/pixel',
    packages=[
        'pixel','pixel.backend','pixel.frontend'
    ],
    package_dir={'pixel':
                 'pixel'},
    entry_points={
        'console_scripts': [
            'pixel=pixel.cli:main'
        ]
    },
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.xml', '*.html', '*.js']
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pixel',
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
