# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 20:54
# @Author  : Yannick
# @File    : exception_demo1.py


def return_test(a):
    try:
        if a <= 0:
            raise ValueError('data can not be negative')
        else:
            return a
    except ValueError as e:
        _msg = str(e) + "Value 2 KeyError."
        raise KeyError(_msg)
    finally:
        print("end finally")
        # 这里有return，则外层调用捕获不到KeyError
        # 这里没有return，则外层调用正常捕获到KeyError
        # return -1

try:
    return_test(0)
except KeyError as e:
    print(e, "exception in call func and exception block.")

# print(return_test(2))
