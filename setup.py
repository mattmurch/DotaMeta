#!/usr/bin/env python3

from setuptools import setup

__version__ = '0.0.0'

setup(name='DotaMeta',
      version=__version__,
      install_requires=['certifi==2017.4.17',
                    'chardet==3.0.4',
                    'dota2api==1.3.3',
                    'idna==2.5',
                    'requests==2.18.1',
                    'urllib3==1.24.2',],
      description='Dota 2 Analytics',
      long_description=open('README.md').read(),
      author='Matt Murch',
      author_email='mattmurch@gmail.com',
      url='https://github.com/mattmurch/DotaMeta',
      download_url='https://github.com/mattmurch/DotaMeta/tarball/' + __version__,
      scripts=['main.py'],
      license='MIT',
      classifiers=[
          
      ],
      keywords=('dota 2 analytics'),
      packages=[],
      )
