# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 21:39
# @Author  : Yannick
# @File    : process_lock_demo.py.py

import multiprocessing
import time


# 有锁，使用上下文管理
def safe_producter(w_lock, f):
    with w_lock:
        fp = open(f, 'a+')
        for i in range(10):
            fp.write("safe_producter :: write {num} to file. \n".format(num=i))
            time.sleep(1)
        fp.close()


def safe_producter1(w_lock, f):
    w_lock.acquire()
    try:
        fp = open(f, 'a+')
        for i in range(10):
            fp.write("safe_producter1 :: write {num} to file. \n".format(num=i))
        fp.close()
    finally:
        w_lock.release()


# 无锁
def unsafe_producter(f):
    fp = open(f, 'a+')
    for i in range(10):
        fp.write("unsafe_producter :: write {num} to file. \n".format(num=i))
    fp.close()


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    log = "process_lock_demo.log"
    sp = multiprocessing.Process(target=safe_producter, args=(lock, log))
    sp1 = multiprocessing.Process(target=safe_producter1, args=(lock, log))
    usp = multiprocessing.Process(target=unsafe_producter, args=(log,))

    sp.start()
    sp1.start()
    usp.start()

    sp.join()
    sp1.join()
    usp.join()

    print("main end ..")

