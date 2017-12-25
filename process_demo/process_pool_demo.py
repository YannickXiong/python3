import multiprocessing
import time


def producer1(data):
    print("producer1 generate data {_data} .. {_time}.".format(_data=data, _time=time.ctime()))
    time.sleep(3)
    print("producer1 :: data {_data} ends .. {_time}.".format(_data=data, _time=time.ctime()))


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=3)
    for i in range(6):
        # apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞，apply(func[, args[, kwds]])是阻塞的
        # 差异体现在：
        #  1. 主进程中print("main ends .. {_time}.".format(_time=time.ctime()))是否等待子里程执行完后再执行
        # pool.apply_async(producer1, (i,))
        pool.apply(producer1, (i,))

    print("main ends .. {_time}.".format(_time=time.ctime()))

    pool.close()
    # close()  关闭pool，使其不在接受新的任务。
    # terminate()  结束工作进程，不在处理未完成的任务。
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print("subprocess ends .. {_time}.".format(_time=time.ctime()))
