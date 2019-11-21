from random import randrange
from random import choice


def randSc():  # 生成100个学生对象
    a1 = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜"
    a3 = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
    a2 = "1234567890"
    stulist = []
    dict1 = []

    for i in range(100):
        obj = objname = choice(a1) + choice(a3)
        obj = Student()
        obj.name = objname
        id1 = '2019'
        for j in range(7):
            id1 += str(choice(a2))
        obj.id = id1
        obj.score = randrange(0, 100)
        stulist.append(obj)

    # 输出学生名字
    '''
    for i in stulist:
        print(i.name)
    '''

    # 返回学生对象列表
    return stulist


def aSort(blist):  # 按属性排序, 怎么用其他排序方法?
    alist = blist
    alist.sort(key=lambda x: x.score, reverse=True)  # 按降序排序
    '''
    for i in alist:
        i.printinfo()
    '''
    return alist


class Student():

    def __init__(self, name='0', id="00000000000", score='0', degree='X'):
        self.name = name
        self.id = id
        self.score = score
        self.degree = degree

    def printinfo(self):  # 打印信息
        print("学生姓名: ", self.name
            , "\n学号: ", self.id
            , "\n英语成绩: ", self.score
            , "\n等级: ", self.degree
            , "\n")


def sortG(ilist):  # 转换五级制

        for i in ilist:
            if i.score >= 80:
                i.degree = 'A'
            elif i.score >= 60:
                i.degree = 'B'
            elif i.score >= 40:
                i.degree = 'C'
            elif i.score >= 20:
                i.degree = 'D'
            else :
                i.degree = 'E'
        '''
        print(ilist)
        '''
        for j in ilist:
            j.printinfo()
        return ilist


sortG(aSort(randSc()))



