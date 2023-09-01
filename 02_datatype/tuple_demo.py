"""
元组：和 list 类似，使用 () 声明，不可修改，性能是 list 的数倍
"""

print('\n----------- tuple 和 list 互相转换 -----------')
T = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L = list(T)
print('列表【list】- ', L)
T_NEW = tuple(L)
print('元组【tuple】-', T_NEW)

print('\n----------- count() 确认元素在 tuple 中出现的次数 -----------')
T = (1, 1, 2, 2, 3, 3, 1, 3, 5, 7, 9)
print(f' 1 出现的次数: {T.count(1)} \n 5 出现的次数: {T.count(5)}')

print('\n----------- index() 确认元素在 tuple 中的位置 -----------')
print('数字 9 在 tuple 中首次出现的位置索引为: ', T.index(9))

print('\n----------- 只有一个元素的 tuple 定义时要加一个逗号 “,”')
T = (1, )
print('不加逗号，() 会被 Python 解析成四则运算符号: ', (1))
print(T)

print('\n----------- tuple 的不可变性只能约束 3 种类型的元素: 数字、布尔、字符串 -----------')
T = (1, 'CH', [3, 4])
print('一个包含 list 的元组 - ', T)
L = T[2]
L[1] = 666
print('list 中的元素被修改后 - ', T)
