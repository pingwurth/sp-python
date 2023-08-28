"""
布尔运算
"""

print('----------- 布尔运算 - 与运算 -----------')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('----------- 布尔运算 - 或运算 -----------')
print(True or True)
print(True or False)
print(False or True)
print(False or False)


print('----------- 布尔运算 - 非运算 -----------')
print(not True)
print(not False)
# not 优先级高高于 and 和 no
print(True and not False)
# Python 把空字符串、0、None 都当作 False，其他数值和非空字符串都当作 True
a = True
print(a and 0 or 99)

print('----------- 布尔运算 - 短路运算 -----------')
a = True
b = False
# 如果 a 是 False，无论 b 是什么，a and b 结果都是 False，所以 and 后面的表达式没必要再计算了
print(a and b)
# 如果 a 是 True，无论 b 是什么，a or b 结果都是 True，所以 or 后面的表达式就没必要再计算了
print(a or b)

print('----------- 短路运算验证示例 -----------')
a = 'Python'
print('hello,', a or 'world')
b = ''
print('hello,', b or 'world')