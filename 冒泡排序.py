from random import randint

list_ = []
for i in range(1, 21):
    list_.append(randint(1, 21))

print(list_)

#  bubbleSort start
a = len(list_)
for i in range(a):  # 每一趟
    for j in range(0, a - i - 1):  # 每趟的交换
        if list_[j] > list_[j + 1]:
            list_[j], list_[j + 1] = list_[j + 1], list_[j]
#  bubbleSort end

print(list_)
