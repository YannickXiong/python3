# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 21:21
# @Author  : Jason Xiong
# @Site    : 
# @File    : process_daemon_demo.py


import multiprocessing
import time


def producer(interval):
    print("producer starts to work at {_time}".format(_time=time.ctime()))
    time.sleep(interval)
    print("producer stops working at {_time}".format(_time=time.ctime()))


if __name__ == "__main__":
    print("the main process begins ..")
    p = multiprocessing.Process(target=producer, args=(2,))
    # p.daemon = True必须在p.start()前面设置
    # 如果设置了p.daemon = True，并且没有join()来阻塞，则主进程退出后，子进程也随着
    # 主进程退出，即使子进程没有执行完，除非显示地使用了join
    p.daemon = True
    p.start()
    print("the main process ends ..")
