# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='nart',
    version='1.0.dev1',
    description='NART: Naver RealTime Keyword',
    author='Keunhyun Oh',
    author_email='ocworld@gmail.com',
    url='https://github.com/ocworld/nart',
    packages=find_packages(exclude=('tests', 'docs')),
    platforms=['any'],
    setup_requires=[
        'pytest-runner==4.4',
    ],
    tests_require=[
        'pytest==4.2',
    ],
    entry_points={
        'console_scripts': ['nart=nart.nart:main'],
    },
    classifiers={
        'Programming Language :: Python',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: News/Diary'
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    },
    project_url={
        'Bug Reports': 'https://github.com/ocworld/nart/issues',
        'Source': 'https://github.com/ocworld/nart'
    }
)