from distutils.core import setup
from vkAPI import __version__, __author__
from os.path import join, dirname

setup(
    name='vkAPI',
    version=__version__,
    packages=['vkAPI'],
    url='https://github.com/sakost/vkAPI',
    license='Apache 2.0',
    author=__author__,
    author_email='sakost01@gmail.com',
    description='Library for interaction with API of vk',
    long_description=open('README.rst').read(),
    test_suite='tests',
    install_requires=[
        'requests==2.9.1'
    ]
)
