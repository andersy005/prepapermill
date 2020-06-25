#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    maintainer='Anderson Banihirwe',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
    description='pre-commit hooks for papermill',
    install_requires=requirements,
    license='MIT license',
    long_description=long_description,
    include_package_data=True,
    keywords='prepapermill',
    name='prepapermill',
    packages=find_packages(include=['prepapermill', 'prepapermill.*']),
    entry_points={'console_scripts': ['prepapermill = prepapermill.core:main']},
    url='https://github.com/andersy005/prepapermill',
    project_urls={
        'Documentation': 'https://github.com/andersy005/prepapermill',
        'Source': 'https://github.com/andersy005/prepapermill',
        'Tracker': 'https://github.com/andersy005/prepapermill/issues',
    },
    zip_safe=False,
)
