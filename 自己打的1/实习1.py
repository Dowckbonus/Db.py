# 1.随机生成分数列表 2.对分数列表排序 3.将排序后列表转换为五级制

from random import randint


def listSc():  # 随机生成100个成绩并输出
    a = [randint(0, 100) for i in range(100)]
    print(a)
    return a


def bs():  # 冒泡排序并输出
    b = listSc()
    c = len(b)
    for i in range(c):
        for j in range(0, c - i - 1):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
    print(b)
    return b


class Transfer():  # 转换类

    def __init__(self, ilist):  # 输入列表参数
        self.ilist = ilist

    def sortG(self):  # 转换五级制
        d = self.ilist
        for i in range(100):
            if i >= 80:
                d[i] = 'A'
            elif i >= 60:
                d[i] = 'B'
            elif i >= 40:
                d[i] = 'C'
            elif i >= 20:
                d[i] = 'D'
            else:
                d[i] = 'E'
        print(d)
        return d


# 执行
Transfer(bs()).sortG()

