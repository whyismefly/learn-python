# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""多线//进程探索"""

from multiprocessing import Process
import os
import time


def run_proc(name):
    print time.time()
    time.sleep(3)
    print 'Run child process %s (%s)...' % (name, os.getpid())


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    processes = list()
    for i in range(5):
        p = Process(target=run_proc, args=('test',))
        print 'Process will start.'
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    print 'Process end.'