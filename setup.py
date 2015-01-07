try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Coding Exercise for Bryan Kappa',
    'author': 'Bryan Kappa',
    'url': 'https://github.com/parappathekappa/setest.git',
    'download_url': 'https://github.com/parappathekappa/setest/archive/master.zip',
    'author_email': 'parappathekappa@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [''],
    'scripts': [],
    'name': 'setest'
}

setup(**config)