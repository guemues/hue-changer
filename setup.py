
from distutils.core import setup
import os


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as _:
        for install in _:
            requirements_list.append(install.strip())

    return requirements_list

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


setup(
  name='huechanger',
  packages=['huechanger'],  # this must be the same as the name above
  version='0.1',
  description='Change color of images',
  long_description=long_description,
  author='Orcun Gumus',
  author_email='orcungumus@gmail.com',
  url='https://github.com/guemues/hue-changer',  # use the URL to the github repo
  download_url='https://github.com/guemues/hue-changer/archive/0.1.tar.gz',  # I'll explain this in a second
  keywords=['color'],  # arbitrary keywords
  install_requires=requirements()
)