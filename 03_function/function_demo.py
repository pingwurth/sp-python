"""
【函数】
"""

# 计算 5 的阶乘
result = 5 * 4 * 3 * 2 * 1
print(result)

# 计算 10 的阶乘
result = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
print(result)

# 计算 20 的阶乘
result = 20 * 19 * 18 * 17 * 16 * 15 * 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
print(result)

print('\n----------- 如何定义函数 -----------')


def factorial(n):
    """
        (⊙_⊙)!!! 计算个阶乘这么麻烦
        用函数把计算逻辑包装起来，变量提取成参数
    :param n: 要计算的阶数
    :return: n 的阶乘
    """
    if type(n) == int:
        ret = 1
        while n > 1:
            ret *= n
            n = n - 1
        return ret


factorial_5 = factorial(5)
print('5 的阶乘：', factorial_5)
factorial_10 = factorial(10)
print('10 的阶乘：', factorial_10)
factorial_20 = factorial(20)
print('20 的阶乘：', factorial_20)

"""
Python 内置函数
"""
print('\n----------- Python 内置函数 -----------')
print('绝对值函数 abs() ---- ', abs(-2))
print('字符串转整数 int() ---- ', int('123'))
print('数字转字符串 str() ---- ', str(1.23))

print('\n----------- 函数可以有多个返回值 -----------')


def sub_sum(li):
    """
    :param li: 一个列表
    :return: {列表的奇数和, 列表的偶数和}
    """
    index = 0
    sum1 = 0
    sum2 = 0
    for item in li:
        if index % 2 == 0:
            sum1 += item
        else:
            sum2 += item
        index += 1
    return sum1, sum2


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sub_sum(L)
print('奇数项的和 = {}'.format(result[0]))
print('偶数项的和 = {}'.format(result[1]))
