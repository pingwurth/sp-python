import math

"""
math 模块演示
"""
print(f'math 模块 ---------- 取绝对值 {math.fabs(-123.0)}')
print(f'math 模块 ---------- 向下取整 {math.floor(-2.5)}')
print(f'math 模块 ---------- 向上取整 {math.ceil(-2.5)}')
print(f'math 模块 ---------- 指数运算：2 的平方 = {math.pow(2, 2)}')
print(f'math 模块 ---------- 平方根运算：√16 = {math.sqrt(16)}')
print(f'math 模块 ---------- 拆分小数和整数：3.1415926 = {math.modf(3.1415926)}')
print(f'math 模块 ---------- 列表元素累加和：[1, 2, 3] = {math.fsum([1, 2, 3])}')
# math.copysign(a, b) 的功能是将参数 b 的正负符号复制给第一个数
print(f'math 模块 ---------- 正负符号传递：{math.copysign(2, -1)}')
print(f'math 模块 ---------- 圆周率 Π = {math.pi}')
print(f'math 模块 ---------- 自然对数常量 e = {math.e}')
