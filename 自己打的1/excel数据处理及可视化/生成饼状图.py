import xlrd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

filename = 'data.xlsx'
workbook = xlrd.open_workbook(filename)
worksheet = workbook.sheet_by_index(0)


# 学生类
class Student:
    def __init__(self, **entries):
        self.__dict__.update(entries)


if __name__ == '__main__':
    # 读取表格
    stu_list = []
    for i in range(worksheet.nrows):
        if i >= 1:
            stu_item = {'id': worksheet.row_values(i)[0],
                        'name': worksheet.row_values(i)[1],
                        'sex': worksheet.row_values(i)[2],
                        'grade': worksheet.row_values(i)[3]}
            stu_item['id'] = Student(**stu_item)
            stu_list.append(stu_item['id'])

    stu_list.sort(key=lambda x: int(x.__dict__['grade']), reverse=False)
    for i in stu_list:
        print(i.__dict__)

    # 输出录取结果
    admit_list_1 = []
    admit_list_2 = []
    for i in range(len(stu_list)):
        if i <= len(stu_list) // 5:
            stu_list[i].__dict__.update({'result': '一本'})
            admit_list_1.append(stu_list[i])
        elif i <= len(stu_list) // 3:
            stu_list[i].__dict__.update({'result': '二本'})
            admit_list_2.append(stu_list[i])
        else:
            stu_list[i].__dict__.update({'result': '未上榜'})
        print(stu_list[i].__dict__['name'], stu_list[i].__dict__['result'])

    print('一本名单：')
    for i in range(len(admit_list_1)):
        print(admit_list_1[i].__dict__['name'], end=' ')
    print('\n二本名单：')
    for j in range(len(admit_list_2)):
        print(admit_list_2[j].__dict__['name'], end=' ')

    # 绘制饼状图
    # 一本
    def pie1(admit_list_1):
        male_1 = 0
        female_1 = 0
        for i in range(len(admit_list_1)):
            if admit_list_1[i].__dict__['sex'] == '男':
                male_1 += 1
            elif admit_list_1[i].__dict__['sex'] == '女':
                female_1 += 1
            else:
                pass

        labels = ['男', '女']
        sizes = [male_1, female_1]

        plt.pie(sizes, labels=labels, autopct='%1.2f%%', shadow=False, startangle=150)
        plt.title('一本男女比例')
        plt.axis('equal')
        plt.show()

    # 二本
    def pie2(admit_list_2):
        male_2 = 0
        female_2 = 0
        for i in range(len(admit_list_2)):
            if admit_list_2[i].__dict__['sex'] == '男':
                male_2 += 1
            elif admit_list_2[i].__dict__['sex'] == '女':
                female_2 += 1
            else:
                pass
        labels = ['男', '女']
        sizes = [male_2, female_2]
        plt.pie(sizes, labels=labels, autopct='%1.2f%%', shadow=False, startangle=150)
        plt.title('二本男女比例')
        plt.axis('equal')
        plt.show()

    pie1(admit_list_1)
    pie2(admit_list_2)