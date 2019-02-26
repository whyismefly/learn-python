
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config={
    'description': 'My Project skeleton',
    'author': 'WHY',
    'url': '...',
    'download_url': '...',
    'author_email': '...',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'skeleton'
}
setup(**config)