print("this is a test of code path in try...except...else...finally")
print("************************************************************")


def exception_test():
    """
    测试有不抛出异常并且有return的时候try ... exception ... finally执行顺序
    :return:
    """
    try:
        print("doing some work, and maybe exception will be raised")
        # raise IndexError("index error")
        # print("after exception raise")
        # return 0    # 如果这里return（并且没有raise异常），则else中代码不会被执行；raise时else也会执行
        # 只有没有异常，并且不return的时候，else才会被执行到
    except KeyError as e:
        print("in KeyError except")
        print(e)
        return 1
    except IndexError as e:
        print("in IndexError except")
        print(e)
        return 2
    except ZeroDivisionError as e:
        print("in ZeroDivisionError")
        print(e)
        return 3
    else:
        print("no exception")
        return 4
    finally:
        print("in finally")
        return 5    # 如果这里注释，则最终返回IndexError块中的return


result_code = exception_test()
print(result_code)
