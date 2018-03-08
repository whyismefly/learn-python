try:
    from  setuptools import setup
except ImportError:
    from distutils.core import setup

config={
    'description':'get stock data',
    'author': 'WHY',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'stock'
}

"""
setup(name='Distutils',
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['distutils', 'distutils.command'],
        INFO='C:\Users\Administrator>pip list
        DEPRECATION: The default format will switch to columns in the future. You can us
        e --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.con
        f under the [list] section) to disable this warning.
        beautifulsoup4 (4.6.0)
        certifi (2018.1.18)
        chardet (3.0.4)
        distribute (0.6.35)
        idna (2.6)
        lpthw.web (1.1)
        lxml (4.1.1)
        nose (1.3.7)
        pip (9.0.1)
        pygame (1.9.3)
        requests (2.18.4)
        selenium (3.8.0)
        setuptools (36.2.7)
        urllib3 (1.22)
        virtualenv (15.1.0)
        '
     )
"""
setup(**config)