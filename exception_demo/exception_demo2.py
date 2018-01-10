def test():
    try:
        a = 2
        return a    # 首先将return的值保存，再执行finally中语句，如果finally中有return，则覆盖这里的return值
    except Exception as e:
        pass

    finally:
        print('finally')
        return 3


s = test()
print(s)    # 注意最后的输出顺序
