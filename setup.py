"""Setuptools entry point."""
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

dirname = os.path.dirname(__file__)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='process-timer',
    version='1.1',
    description='Celery Timeout decorator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Siddharth Prajosh',
    author_email='sprajosh@gmail.com',
    url='https://github.com/sprajosh/process-timer',
    packages=['process_timer'],
    install_requires=['billiard'],
    classifiers=CLASSIFIERS
)
