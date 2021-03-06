"""
 CLI for arcsecond.io
"""
import ast
import re

from setuptools import find_packages, setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('agroop/__init__.py', 'rb') as f:
    __version__ = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))

setup(
    name='agroop',
    version=__version__,
    url='https://github.com/arcsecond-io/agroop',
    license='MIT',
    author='Cedric Foellmi',
    author_email='cedric@arcsecond.io',
    description='agroop = *a*pproximative *gr*ep for c*oo*rdinates...',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'click>=7',
        'astropy>=3',
        'arcsecond>=0.6.2'
    ],
    entry_points={
        'console_scripts': [
            'agroop = agroop.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
