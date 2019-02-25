try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config={
    'description':'ex49',
    'author': 'WHY',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'ex49'
}
setup(**config)
