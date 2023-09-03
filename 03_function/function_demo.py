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

print('\n----------- 递归函数 -----------')


def fact(n):
    """
    计算 n 的阶乘
    :param n: 阶数
    :return: n 的阶乘
    """
    if n == 1:
        return 1
    return n * fact(n - 1)


print('使用递归函数实现：计算 !5 = ', fact(5))

print('\n----------- 函数参数校验 -----------')


def func(x):
    """
    如果 x 是 list 或 tuple，就计算所有数字的和
    :param x: 一个列表或元组，如果不是就返回 None
    :return: x 中所有数字求和结果
    """
    if not isinstance(x, list) and not isinstance(x, tuple):
        return None
    # x 是一个 列表，计算所有数字的和
    if type(x) == list:
        ret = 0
        for item in x:
            if isinstance(item, int) or isinstance(item, float):
                ret = ret + item
        return ret
    # x 是一个 元组，计算所有数字的和
    if type(x) == tuple:
        ret = 0
        for item in x:
            if isinstance(item, int) or isinstance(item, float):
                ret = ret + item
        return ret


li = [1, 2, 3, 4, 5]
print(func(li))

print('\n----------- 默认参数（必须定义在最后，否则参数匹配会有问题） -----------')


def greet(name='World'):
    print('Hello,', name)


greet()
greet('Python')

print('\n----------- 可变参数（参数被当作 tuple 处理） -----------')


def average(*args):
    """
    计算平均数
    :param args: 一组数字
    :return: 平均数
    """
    count = 0
    if len(args) == 0:
        return count
    for item in args:
        count += item
    avg = count / len(args)
    return avg


print(average(2, 4, 6, 7, 9))

print('\n----------- 可变关键字参数（参数被当作 dict 处理） -----------')


def info(**kwargs):
    names = kwargs['names']
    gender_list = kwargs['gender']
    age_list = kwargs['age']
    index = 0
    for name in names:
        gender = gender_list[index]
        age = age_list[index]
        print('name: {}, gender: {}, age: {}'.format(name, gender, age))
        index += 1


info(names=['Alice', 'Bob', 'Candy'],
     gender=['girl', 'boy', 'girl'],
     age=[16, 17, 15])


print('\n----------- 参数定义顺序：必传参数 -> 默认参数 -> 可变参数 -> 可变关键字参数 -----------')
