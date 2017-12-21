import multiprocessing
import time


def producer1(queue):
    i = 0
    while i <= 50:
        try:
            print("producer1 generated data {_data} into queue.".format(_data=i))
            # put指定了block，则必须指定timeout，否则不超时一直等待形成死锁
            queue.put(i, block=True, timeout=1)
            i += 1
            time.sleep(1)
        except Exception as e:
            print("producer1 found exception => ", e)


def consumer1(queue):
    while True:
        try:
            _data = queue.get(block=True, timeout=1)
            print("consumer1 got data {_data} from queue.".format(_data=_data))
            time.sleep(3)
        except Exception as e:
            print("consumer1 found exception => ", e)


if __name__ == "__main__":
    queue = multiprocessing.Queue(maxsize=10)
    p1 = multiprocessing.Process(target=producer1, args=(queue,))
    c1 = multiprocessing.Process(target=consumer1, args=(queue,))
    p1.start()
    c1.start()

    p1.join()
    c1.join()
