#!/usr/bin/python3
a = float(input("请输入第1家金额："))
b = float(input("请输入第2家金额："))
c = float(input("请输入第3家金额："))
average = (a + b + c) / 3
print("平均值运算结果为：",  '%.2f' % average)

# a的偏差率
dev1 = ((a - average) / average) * 100

print("第1家的偏差率为：", '%.2f' % dev1, "%")

# b的偏差率
dev2 = ((b - average) / average) * 100
print("第2家的偏差率为：", '%.2f' % dev2, "%")

# c的偏差率
dev3 = ((c - average) / average) * 100
print("第3家的偏差率为：", '%.2f' % dev3, "%")

i = 1
for dev in [dev1, dev2, dev3]:  # 迭代 三家 偏差

    if dev > 2:
        print("抱歉，第", i, "家偏差大于2%减少分数为：",  dev//2)
        i = i+1
    elif dev < -2:
        print('抱歉，第', i, '家偏差小于2%减少分数为：', (abs(dev)//2)*0.5)
        i = i+1
    else:
        print('恭喜第', i, '家得分30分')
        i = i+1
