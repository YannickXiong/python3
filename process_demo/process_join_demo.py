# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 21:09
# @Author  : Jason Xiong
# @Site    : 
# @File    : process_join_demo.py

import multiprocessing
import time


class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("the time is {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1

if __name__ == '__main__':
    print("the main process begins ..")
    p = ClockProcess(1)
    p.start()
    # p.join()的作用就是让主进程阻塞，即主进程必须等子进行结束后才继续
    # 如果没有join()，则主进程会自己先执行
    p.join()
    print("the main process end ..")
