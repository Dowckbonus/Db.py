filename = "f2.txt"
student1 = []


class Student():  # 学生类

    def __init__(self, id='00000000', name='xxx', sex='x', score='000'):
        self.id = id
        self.name = name
        self.sex = sex
        self.score = score
        self.grade = 'x'

    '''
    def printInfo(self):
        print([self.id, self.name, self.sex, self.score])
    '''


def cScore(stulist):  # 导入排序后的列表
    scorelist = list(map(lambda x: x.score, student1))
    list1 = list2 = list3 = list4 = ''
    alist1 = alist2 = alist3 = alist4 = []
    blist1 = blist2 = blist3 = ''

    rank1 = len(scorelist) // 10
    rank2 = len(scorelist) // 5
    rank3 = len(scorelist) // 3
    line1 = scorelist[rank1]
    line2 = scorelist[rank2]
    line3 = scorelist[rank3]
    print("分数线:", "\n一本线： ", line1, "\n二本线： ", line2, "\n专科线： ", line3)

    for i in stulist:  # 各分数段名单
        if i.score >= line1:
            list1 += i.name + " "
        elif i.score >= line2:
            list2 += i.name + " "
        elif i.score >= line3:
            list3 += i.name + " "
        else:
            list4 += i.name + " "
    print("各分数段名单:", "\n一本线： ", list1, "\n二本线： ", list2, "\n专科线： ", list3, "\n未上榜： ", list4)

    for i in stulist:  # 名字/性别计数列表
        if i.score >= line1:
            list1 += i.name + " "
            blist1 += i.sex + ''
        elif i.score >= line2:
            list2 += i.name + " "
            blist2 += i.sex + ''
        elif i.score >= line3:
            list3 += i.name + " "
            blist3 += i.sex + ''
        else:
            list4 += i.name + " "

    blist1.split()
    blist2.split()
    blist3.split()

    print(
        "各分数段男女性别比例：",
        "\n一本线:",
        sexSort(blist1),
        "\n二本线:",
        sexSort(blist2),
        "\n专科线:",
        sexSort(blist3))


def sexSort(num):  # 计算性别比例

    sum1 = sum2 = 0
    for i in num:
        if i == '男':
            sum1 += 1
        elif i == '女':
            sum2 += 1
    return (sum1 / sum2)


with open(filename) as f2:  # 打开学生名单
    stulist = f2.readlines()

for x in stulist:  # 通过学生名单生成学生对象列表

    a = x.split()
    id = a[0]
    name = stu = a[1]
    sex = a[2]
    score = a[3]

    stu = Student()
    stu.score = score
    stu.id = id
    stu.name = name
    stu.sex = sex
    student1.append(stu)

student1.sort(key=lambda x: x.score, reverse=True)  # 按分数排序学生

'''
print(list(map(lambda x:x.score, student1)))
print(list(map(lambda x:x.name, student1)))
'''

cScore(student1)
