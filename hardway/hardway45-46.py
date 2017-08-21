#!/usr/bin/python
# encoding:utf-8

"""
45课程直接跳过了，后期会补充一个小游戏，
46在安装过程中遇到了不少问了，折腾了几个小时，实在汗颜...
现在把46安装过程复制一下
"""
# 1.     pip from http://pypi.python.org/pypi/pip
# 2.     distribute from http://pypi.python.org/pypi/distribute
# 3.     nose from http://pypi.python.org/pypi/nose
# 4.     virtualenv from http://pypi.python.org/pypi/virtualenv
#
#setuptools--->distribute  easy_install--->pip
#-------------------------------------------------------------------------
"""
pip已经在python2.7中自带无需下载，后三个官网下载，可以在后面操作前先更新一下
"""
"""
Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>cd D:\PYTHON\Python27\Scripts

C:\Users\Administrator>d:

D:\PYTHON\Python27\Scripts>pip -help

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependen
cies.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring
                              environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be
                              used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be
                              used up to 3 times (corresponding to WARNING,
                              ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form
                              [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should
                              attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists:
                              (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host as trusted, even though it does
                              not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file
                              containing the private key and the certificate
                              in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine
                              whether a new version of pip is available for
                              download. Implied with --no-index.

D:\PYTHON\Python27\Scripts>python -m pip install -U pip
Requirement already up-to-date: pip in d:\python\python27\lib\site-packages

D:\PYTHON\Python27\Scripts>
"""
#-------------------------------------------------------------------------
"""
安装distribute，安装之前一定要先卸载安装下setuptools，不然会出来很多问题，比如什么找不到platform名字之类的
每个人电脑环境不同，情况也会有所变化
"""

"""
Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>cd D:\PYTHON\distribute-0.6.49

C:\Users\Administrator>d:

D:\PYTHON\distribute-0.6.49>python distribute_setup.py install
Downloading http://pypi.python.org/packages/source/d/distribute/distribute-0.6.4
9.tar.gz
Extracting in c:\users\admini~1\appdata\local\temp\tmpn3jiax
Now working in c:\users\admini~1\appdata\local\temp\tmpn3jiax\distribute-0.6.49
Installing Distribute
Before install bootstrap.
Scanning installed packages
Setuptools installation detected at d:\python\python27\lib\site-packages
Non-egg installation
Could not locate setuptools*.egg-info
Traceback (most recent call last):
  File "setup.py", line 232, in <module>
    scripts = scripts,
  File "D:\PYTHON\Python27\lib\distutils\core.py", line 111, in setup
    _setup_distribution = dist = klass(attrs)
  File "c:\users\admini~1\appdata\local\temp\tmpn3jiax\distribute-0.6.49\setupto
ols\dist.py", line 225, in __init__
    _Distribution.__init__(self,attrs)
  File "D:\PYTHON\Python27\lib\distutils\dist.py", line 287, in __init__
    self.finalize_options()
  File "c:\users\admini~1\appdata\local\temp\tmpn3jiax\distribute-0.6.49\setupto
ols\dist.py", line 257, in finalize_options
    ep.require(installer=self.fetch_build_egg)
  File "c:\users\admini~1\appdata\local\temp\tmpn3jiax\distribute-0.6.49\pkg_res
ources.py", line 2099, in require
    working_set.resolve(self.dist.requires(self.extras),env,installer))
  File "c:\users\admini~1\appdata\local\temp\tmpn3jiax\distribute-0.6.49\pkg_res
ources.py", line 2309, in requires
    dm = self._dep_map
  File "c:\users\admini~1\appdata\local\temp\tmpn3jiax\distribute-0.6.49\pkg_res
ources.py", line 2538, in _dep_map
    self.__dep_map = self._compute_dependencies()
  File "c:\users\admini~1\appdata\local\temp\tmpn3jiax\distribute-0.6.49\pkg_res
ources.py", line 2571, in _compute_dependencies
    common = frozenset(reqs_for_extra(None))
  File "c:\users\admini~1\appdata\local\temp\tmpn3jiax\distribute-0.6.49\pkg_res
ources.py", line 2568, in reqs_for_extra
    if req.marker_fn(override={'extra':extra}):
  File "c:\users\admini~1\appdata\local\temp\tmpn3jiax\distribute-0.6.49\_marker
lib\markers.py", line 109, in marker_fn
    return eval(compiled_marker, environment)
  File "<environment marker>", line 1, in <module>
NameError: name 'sys_platform' is not defined
Something went wrong during the installation.
See the error message above.

D:\PYTHON\distribute-0.6.49>
"""
#直接暗转出现了Non-egg installation
#Could not locate setuptools*.egg-info
# NameError: name 'sys_platform' is not defined
#需要重新安装setuptools

"""
由于数据太多只写指令setep下载过了，不过不下载可以通过指令卸载在安装
pip uninstall setuptools
cd D:\PYTHON\setuptools-36.2.7
D:
python setup.py install
"""

"""
cd D:\PYTHON\distribute-0.6.49
D:
python distribute_setup.py install
running build_py
"""

#-------------------------------------------------------------------------

"""
安装nose
"""

"""
cd D:\PYTHON\nose-1.3.7\nose-1.3.7
D:
python setup.py install
running build_py
"""

#-------------------------------------------------------------------------
"""
安装virtualenv
"""

"""
Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>cd D:\PYTHON\virtualenv-15.1.0\virtualenv-15.1.0

C:\Users\Administrator>d:

D:\PYTHON\virtualenv-15.1.0\virtualenv-15.1.0>python virtualenv.py install
New python executable in D:\PYTHON\virtualenv-15.1.0\virtualenv-15.1.0\install\S
cripts\python.exe
Installing setuptools, pip, wheel...done.

D:\PYTHON\virtualenv-15.1.0\virtualenv-15.1.0>python setup.py install
running install
running bdist_egg
running egg_info
writing virtualenv.egg-info\PKG-INFO
writing top-level names to virtualenv.egg-info\top_level.txt
writing dependency_links to virtualenv.egg-info\dependency_links.txt
writing entry points to virtualenv.egg-info\entry_points.txt
reading manifest file 'virtualenv.egg-info\SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no previously-included files matching '*' found under directory 'docs\_
templates'
warning: no previously-included files matching '*' found under directory 'docs\_
build'
writing manifest file 'virtualenv.egg-info\SOURCES.txt'
installing library code to build\bdist.win32\egg
running install_lib
running build_py
creating build
creating build\lib
copying virtualenv.py -> build\lib
creating build\lib\virtualenv_support
copying virtualenv_support\__init__.py -> build\lib\virtualenv_support
copying virtualenv_support\argparse-1.4.0-py2.py3-none-any.whl -> build\lib\virt
ualenv_support
copying virtualenv_support\pip-9.0.1-py2.py3-none-any.whl -> build\lib\virtualen
v_support
copying virtualenv_support\setuptools-28.8.0-py2.py3-none-any.whl -> build\lib\v
irtualenv_support
copying virtualenv_support\wheel-0.29.0-py2.py3-none-any.whl -> build\lib\virtua
lenv_support
creating build\bdist.win32
creating build\bdist.win32\egg
copying build\lib\virtualenv.py -> build\bdist.win32\egg
creating build\bdist.win32\egg\virtualenv_support
copying build\lib\virtualenv_support\argparse-1.4.0-py2.py3-none-any.whl -> buil
d\bdist.win32\egg\virtualenv_support
copying build\lib\virtualenv_support\pip-9.0.1-py2.py3-none-any.whl -> build\bdi
st.win32\egg\virtualenv_support
copying build\lib\virtualenv_support\setuptools-28.8.0-py2.py3-none-any.whl -> b
uild\bdist.win32\egg\virtualenv_support
copying build\lib\virtualenv_support\wheel-0.29.0-py2.py3-none-any.whl -> build\
bdist.win32\egg\virtualenv_support
copying build\lib\virtualenv_support\__init__.py -> build\bdist.win32\egg\virtua
lenv_support
byte-compiling build\bdist.win32\egg\virtualenv.py to virtualenv.pyc
byte-compiling build\bdist.win32\egg\virtualenv_support\__init__.py to __init__.
pyc
creating build\bdist.win32\egg\EGG-INFO
copying virtualenv.egg-info\PKG-INFO -> build\bdist.win32\egg\EGG-INFO
copying virtualenv.egg-info\SOURCES.txt -> build\bdist.win32\egg\EGG-INFO
copying virtualenv.egg-info\dependency_links.txt -> build\bdist.win32\egg\EGG-IN
FO
copying virtualenv.egg-info\entry_points.txt -> build\bdist.win32\egg\EGG-INFO
copying virtualenv.egg-info\not-zip-safe -> build\bdist.win32\egg\EGG-INFO
copying virtualenv.egg-info\top_level.txt -> build\bdist.win32\egg\EGG-INFO
creating dist
creating 'dist\virtualenv-15.1.0-py2.7.egg' and adding 'build\bdist.win32\egg' t
o it
removing 'build\bdist.win32\egg' (and everything under it)
Processing virtualenv-15.1.0-py2.7.egg
creating d:\python\python27\lib\site-packages\virtualenv-15.1.0-py2.7.egg
Extracting virtualenv-15.1.0-py2.7.egg to d:\python\python27\lib\site-packages
Adding virtualenv 15.1.0 to easy-install.pth file
Installing virtualenv-script.py script to D:\PYTHON\Python27\Scripts
Installing virtualenv.exe script to D:\PYTHON\Python27\Scripts

Installed d:\python\python27\lib\site-packages\virtualenv-15.1.0-py2.7.egg
Processing dependencies for virtualenv==15.1.0
Finished processing dependencies for virtualenv==15.1.0

D:\PYTHON\virtualenv-15.1.0\virtualenv-15.1.0>

"""