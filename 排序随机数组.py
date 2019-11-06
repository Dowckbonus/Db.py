#通过fc()输入一串字符串以生成相应排序后的随机数组

from random import randint


class List():


    b = '_'

    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.x = [randint(1, 101) for i in range(self.num)]  # 按字符长度生成相应长度随机数组

    def pn(self):  #名称迭代 & 打印名称
        print(list(self.name))
        b = iter(list(self.name))
        for i in range(self.num):
            try:
                print(next(b))
            except:
                print("error")
                break

    def bs(self):  # 冒泡
        a = self.num
        for i in range(a):
            for j in range(0, a - i - 1):
                if self.x[j] > self.x[j+1]:
                    self.x[j], self.x[j+1] = self.x[j+1], self.x[j]
        print(self.x)
        return(self)




def fc(f1):  # 打印排序后数组并返回相应实例
    return List(f1, len(f1)).bs()


blist = fc('askdkashdkjashdajshdoajshdoaisdna')
blist.pn()

c = map(lambda x, y: [x, y], blist.name, blist.x)  # 通过lambda生成二维列表
print(dict(c))  # 打印通过二维列表生成的字典 （字典键不能重复，后添加的值覆写前添加的值）
