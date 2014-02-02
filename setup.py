from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


install_requires = [
	'skype4py',
]

setup(
	name='GerSkyBot',
	version='1.0',
	description='Gerrit-Skype Bot',
	author='Vinaya Mandke',
	author_email='vinaya.mandke@synerzip.com',
	install_requires=install_requires,
     )
