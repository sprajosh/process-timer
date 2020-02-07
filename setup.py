"""Setuptools entry point."""
import codecs
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

long_description = (
    codecs.open(os.path.join(dirname, 'README.md'), encoding='utf-8').read()
    )

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
