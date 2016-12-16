try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url':"WHere to download it.",
    'author_email': 'Myemail.',
    'version': '0.1'
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name':'projectname'
}

setup (**config)
