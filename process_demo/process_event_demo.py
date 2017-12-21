import multiprocessing
import time


def connect_server(event, index):
    print("connect_server :: client {_index} wait to connect to server .. {_time}"
          .format(_time=time.ctime(), _index=index))
    print("connect_server :: client {_index} event.is_set() -> {_state}"
          .format(_index=index, _state=str(event.is_set())))
    # event.wait()会阻塞当前进程，并且是永远阻塞，此时is_set默认为False
    event.wait()
    print("connect_server :: client {_index} connect to server successfully .. {_time}"
          .format(_time=time.ctime(), _index=index))
    print("connect_server :: client {_index} event.is_set() -> {_state}"
          .format(_index=index, _state=str(event.is_set())))


def connect_server_timeout(event, timeout):
    print("")
    print("connect_server_timeout :: wait to connect to server .. {_time}".format(_time=time.ctime()))
    print("connect_server_timeout :: event.is_set() ->", str(event.is_set()))
    # event.wait(timeout)会阻塞当前进程，但是在timeout指定时间后超过
    event.wait(timeout)
    print("connect_server_timeout :: connect to server successfully .. {_time}".format(_time=time.ctime()))
    print("connect_server_timeout :: event.is_set() ->", str(event.is_set()))
    print("")


if __name__ == "__main__":
    e = multiprocessing.Event()
    for i in range(5):
        client1 = multiprocessing.Process(target=connect_server, args=(e, i))
        client1.start()

    # 这里sleep1完全是因为client1和client2在wait前的打印顺序是随机的，加了sleep保证client1总在前面
    time.sleep(1)

    client2 = multiprocessing.Process(target=connect_server_timeout, args=(e, 2))
    client2.start()

    time.sleep(3)
    print("main :: server start up .. {_time}".format(_time=time.ctime()))
    time.sleep(3)
    # 显示的设置，会使event.is_set()由False变成True，从而唤醒前面被阻塞的进程。
    # 多个进程同时被唤醒
    # 这是典型的观察者模式
    e.set()
