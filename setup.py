#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: Put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(crotty-d ): Put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: Put package test requirements here
]

setup(
    name='flask_platform',
    version='0.1.0',
    description="Minimal flask platform",
    long_description=readme + '\n\n' + history,
    author="Darragh Crotty",
    author_email='darragh@darraghcrotty.com',
    url='https://github.com/crotty-d/flask_platform',
    packages=['flask_platform'],
    entry_points={
        'console_scripts': [
            'flask_platform=flask_platform.run:main',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='flask_platform',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
