# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 20:47
# @Author  : Yannick
# @File    : process_pipe_demo.py


import multiprocessing
import time


def producer1(pipesig, maxlen):
    i = 0
    try:
        while i < maxlen:
            print("producer1 send data {_data} into pip .. {_time}"
                  .format(_data=i, _time=time.ctime()))
            pipesig[0].send(i)
            time.sleep(1)
            i += 1
    except Exception as e:
        print("producer1 meet an exception : ", e)
    finally:
        pipesig[0].close()


def consumer1(pipesig):
    try:
        while True:
            _data = pipesig[1].recv()
            print("consumer1 receive data {_data} from pip .. {_time}"
                  .format(_data=_data, _time=time.ctime()))
            time.sleep(1)
    except Exception as e:
        print("consumer1 meet an exception : ", e)
    finally:
        pipesig[1].close()


if __name__ == "__main__":
    pipe = multiprocessing.Pipe()  # default duplex = True
    maxTimes = 5
    """
    1. pipe 返回一个tuple(connection1, connection2)，代表管道的两端
    2. pipe = multiprocessing.Pipe(duplex=)，当duplex为True时，管道两端都能读和写
    3. 当duplex为False时，connection1只负责recv，connection2只负责send
    4. 如果没有消息可接收，recv方法会一直阻塞。如果管道已经被关闭，那么recv方法会抛出EOFError
    """
    p1 = multiprocessing.Process(target=producer1, args=(pipe, maxTimes))
    p2 = multiprocessing.Process(target=consumer1, args=(pipe,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("main ends ..", time.ctime())
