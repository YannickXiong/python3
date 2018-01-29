#! -*- coding:utf-8 -*-


# to test when to return to True in Python
def verify_bool(arg=None):
    ret = bool(arg)

    if arg == "":
        name = "empty string"
        print("%s => %s" % (name, ret))
    else:
        print("%s => %s" % (arg, ret))


class Test:

    def __len__(self):
        return 0


class Test1:
    def __len__(self):
        return 1


# None is False
verify_bool()

# empty dict is False
verify_bool(arg={})
verify_bool(arg=dict())
verify_bool(arg={1: "ok"})

# empty list is False
verify_bool(arg=[])
verify_bool(arg=list())
verify_bool(arg=[1, 2, 3])

# empty tuple is False
verify_bool(arg=())
verify_bool(arg=tuple())
verify_bool(arg=(1,))

# empty set is False
verify_bool(arg=set())
verify_bool(arg={1, 2, 3})

# 只要不是0，都是True
verify_bool(arg=0)
verify_bool(arg=0.34)
verify_bool(arg=1)
verify_bool(arg=1.0)
verify_bool(arg=1.1)
verify_bool(arg=-1)
verify_bool(arg=-0.42)
verify_bool(arg=-1.0)

# 空字符串是False
verify_bool(arg='')
verify_bool(arg="")
verify_bool(arg="Test")

# __len__返回0的是False，返回1的是True
verify_bool(arg=Test) # 所有的类（非实例，当然类属于元类的实例）居然都返回True
verify_bool(arg=Test())
verify_bool(arg=Test1)
verify_bool(arg=Test1())




