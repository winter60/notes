# 用梯度下降法求函数最小值: L=x1^2 + 2x2^2
import matplotlib.pyplot as plt

m = 0.01
x1 = 1
x2 = 3
L = x1 ** 2 + 2*x2**2
times = 0
err = 1

threshold = 0.0000001
values = []

while err > threshold :#and times < 100
    x1 = x1 - m * 2 * x1
    x2 = x2 - m * 4 * x2
    newL = x1 ** 2 + 2*x2**2
    err = abs(newL - L)
    values.append(err)
    L = newL
    times += 1

print(x1,x2,L,times)
plt.plot(values)
plt.show()


# 缺点：
'''
1. 初值敏感
2. 学习率敏感
3. 无法保证是全局最值
'''