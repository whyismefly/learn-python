#!/usr/bin/python
# encoding:utf-8

"""
PS C:\Users\Administrator> cd E:\learn\GitHub\learn-python\hardway\projects\hardway52\gothonweb
PS E:\learn\GitHub\learn-python\hardway\projects\hardway52\gothonweb> nosetests
.E
======================================================================
ERROR: Failure: ImportError (No module named ex47.game)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "e:\learn\python2.7\lib\site-packages\nose\loader.py", line 418, in loadTestsFromName
    addr.filename, addr.module)
  File "e:\learn\python2.7\lib\site-packages\nose\importer.py", line 47, in importFromPath
    return self.importFromDir(dir_path, fqname)
  File "e:\learn\python2.7\lib\site-packages\nose\importer.py", line 94, in importFromDir
    mod = load_module(part_fqname, fh, filename, desc)
  File "E:\learn\GitHub\learn-python\hardway\projects\hardway52\gothonweb\tests\map_tests.py", line 11, in <module>
    from ex47.game import Room
ImportError: No module named ex47.game

----------------------------------------------------------------------
Ran 2 tests in 0.738s

FAILED (errors=1)
PS E:\learn\GitHub\learn-python\hardway\projects\hardway52\gothonweb> nosetests
....
----------------------------------------------------------------------
Ran 4 tests in 0.431s

OK
PS E:\learn\GitHub\learn-python\hardway\projects\hardway52\gothonweb>

"""