import asyncio
import functools

# 参考： http://python.jobbole.com/87541/

# 概念
# event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
# coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。
# 协程对象需要注册到事件循环，由事件循环调用。
# task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。
# future： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别
# async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。

# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。
# 为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
# 请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
#     1.把@asyncio.coroutine替换为async；
#     2.把yield from替换为await。


async def do_some_work1(msg):
    print("do_some_work1 waiting: " + str(msg))
    await asyncio.sleep(1)


@asyncio.coroutine
def do_some_work2(msg):
    print("do_some_work2 waiting: " + str(msg))
    yield from asyncio.sleep(1)


loop1 = asyncio.get_event_loop()
t1 = do_some_work1("using async")

# do_some_work1 是一个携程函数，它返回一个携程对象
print("iscoroutinefunction(do_some_work1) => ", asyncio.iscoroutinefunction(do_some_work1))
print("iscoroutinefunction(t1) => ", asyncio.iscoroutinefunction(t1))
# t1是一个携程对象
print("iscoroutine(t1) => ", asyncio.iscoroutine(t1))

print("isfuture(t1) => ", asyncio.isfuture(t1))
print("-"*25)

t2 = do_some_work1("using @syncio.coroutine")
tasks = [t1, t2]

# 注意：run_until_complete的参数必须是一个future对象，或者是一个awaitable对象，或者是一个携程。
# 这里task显示不是这三者，可以通过asyncio.wait()变成一个awaitable对象。
# 下面的loop2中，一个是携程作为参数，一个是future作为参数，所以没有必要加asyncio.wait()
loop1.run_until_complete(asyncio.wait(tasks))

# 如果这里关闭当前这个线程的默认event_loop，就算下面使用loop2 = asyncio.get_event_loop()，也会报错
# 这里如果不关闭，下面继续使用loop也没关系，不用得命名为loop2
# loop1.close()

print("-"*25)
loop2 = asyncio.get_event_loop()
# run_until_complete 的参数是一个 future，但是我们这里传给它的却是协程对象
loop2.run_until_complete(do_some_work1("run_until_complete(coroutine_obj)"))
# 之所以能这样，是因为它在内部做了检查，通过 ensure_future 函数把协程对象包装
future1 = asyncio.ensure_future(do_some_work2("run_until_complete(future_obj)"))
loop2.run_until_complete(future=future1)

print("-"*25)

# 会生产告警，暂时注释掉，知道它不是一个future就行
# print("isfuture(do_some_work1(\"run_until_complete(coroutine_obj)\") => ",
#       asyncio.isfuture(do_some_work1("run_until_complete(coroutine_obj)")))
print("isfuture(future1 => ", asyncio.isfuture(future1))

print("-"*25)


# 回调
def work_done_call_back(job):
    print("Work {_job} is done, result is {_result}".format(_job=job, _result=job.result()))


# 当回调函数有多个参数的时候，需要以偏函数的方式传入参数，当然，job不需要传，在回调的时候自动传入
# 注意两点：
# 第一、job只能作为最后一个位置参数
def work_done_call_back2(t, alive, job,):
    print("args, time = {_time}, job = {_job}, alive = {_alive}".format(_time=t, _job=job, _alive=alive))
    print("Work {_job} is done, result is {_result}".format(_job=job, _result=job.result()))


future2 = asyncio.ensure_future(do_some_work2("call back test"))
# 注意这里work_done_call_back不能传入参数，否则会抛出异常。
# 观察最终打印出来的结果，想想work_done_call_back是怎么被调用的？
future2.add_done_callback(work_done_call_back)
# 第二点：偏函数不能写成functools.partial(work_done_call_back2, t=2, alive=True)，
# 因为work_done_call_back2就未定义关键字参数！
future2.add_done_callback(functools.partial(work_done_call_back2, 2, True))
loop2.run_until_complete(future2)


print("-"*25)

# 多个携程在同一个loop里，2种方式
#   1. 前面已使用过了，使用asyncio.wait封装tasks；
#   2. 使用asyncio.gather

t3 = do_some_work1("using gather")
t4 = do_some_work2("using gather")
tasks2 = [t3, t4]
# 注意这里有一个开箱的过程
loop2.run_until_complete(asyncio.gather(*tasks2))
# 更直接的，直接将携程传给gather
loop2.run_until_complete(asyncio.gather(do_some_work1("using gather directly"), do_some_work2("using gather directly")))

print("-"*25)

# loop.create_task
task3 = loop2.create_task(do_some_work2("using loop.create_task"))
loop2.run_until_complete(task3)

loop2.close()
