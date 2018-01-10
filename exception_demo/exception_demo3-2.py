print("this is a test of code path in try...except...else...finally")
print("************************************************************")


def exception_test():
    """
    测试有return的时候try ... exception ... finally执行顺序
    :return:
    """
    try:
        print("doing some work, and maybe exception will be raised")
        raise IndexError("index error")
        # print("after exception raise")
        return 0    # try中raise的的代码是不会执行的，所以这里的return是unreachable
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
