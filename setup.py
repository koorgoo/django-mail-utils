#!/usr/bin/env python
from setuptools import setup


setup(
    name='django-mail-utils',
    version='0.3',
    description='Django mail mixins and utilities',
    long_description=open('README.rst').read(),
    author='Dima Kurguzov',
    author_email='koorgoo@gmail.com',
    url='https://github.com/koorgoo/django-mail-utils/',
    license='MIT',
    packages=['mail_utils'],
    install_requires=['django'],
    classifiers=[
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
)
