import multiprocessing
import time
import threading

'''
 1. semaphore本质是一个计数器，当值为0时则阻塞当前进程，直到下一次调用semaphore.release()
 2. semaphore.acquire()使计数器 -1
 3. semaphore.release()使计数器 +1
 4. 所以对比producer_with_semaphore()和producer()发现，使用了semaphore计数器会使限制线程同一时间最多保持
    s = multiprocessing.Semaphore(3)即3个
 5. 同要是不使用semaphore计数器，对比producer()和foo()可以看出，multiprocessing.Process和threading.Thread
    处理还是有不同的，
'''


def producer_with_semaphore(semaphore):
    semaphore.acquire()
    time.sleep(1)
    print("producer_with_semaphore works .. time {_time}.".format(_time=time.ctime()))
    semaphore.release()


def producer():
    time.sleep(1)
    print("producer works .. time {_time}.".format(_time=time.ctime()))


def foo():
    time.sleep(1)   # 程序休息2秒
    print("foo ..", time.ctime())


def foo_with_semaphore(semaphore):
    semaphore.acquire()
    time.sleep(1)
    print("foo with semaphore..", time.ctime())
    semaphore.release()


if __name__ == "__main__":
    s = multiprocessing.Semaphore(3)
    print("producer_with_semaphore ..")
    for i in range(12):
        p1 = multiprocessing.Process(target=producer_with_semaphore, args=(s,))
        p1.start()

    time.sleep(5)
    print("producer_without_semaphore ..")
    for i in range(12):
        p2 = multiprocessing.Process(target=producer(), args=())
        p2.start()

    print("foo ..")
    for i in range(12):
        t1 = threading.Thread(target=foo, args=())  # 实例化一个线程
        t1.start()  # 启动线程

    time.sleep(2)
    s1 = threading.Semaphore(3)
    print("foo with semaphore ..")
    for i in range(12):
        t2 = threading.Thread(target=foo_with_semaphore, args=(s1,))
        t2.start()
