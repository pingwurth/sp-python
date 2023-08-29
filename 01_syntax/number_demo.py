"""
四则运算
"""
print('\n----------- 四则运算 -----------')
num1 = 10
num2 = 0.5

# 加法
result = num1 + num2
print(result)

# 减法
result = num1 - num2
print(result)

# 乘法
result = num1 * num2
print(result)

# 除法
result = num1 / num2
print(result)

"""
取模运算
"""
print('\n----------- 取模运算 -----------')
print(3 % 2)
print(33 % 10)
print(90 % 30)

"""
地板除：结果只保留整数，舍弃小数位
"""
print('\n----------- 地板除：结果只保留整数，舍弃小数位 -----------')
print(10 // 4)
print(10 // 2.5)
print(10 // 3)

"""
保留两位小数
"""
print('\n----------- 保留两位小数 -----------')
print(
    round(10/3, 2)
)

"""
示例：一个长方形的长为 3.14cm，宽为 1.57cm，请计算这个长方形的面积，保留小数点后两位。
"""
print('\n----------- 示例：计算长方形面积 -----------')
length = 3.14
width = 1.57
area = round(length * width, 2)
print(area)
