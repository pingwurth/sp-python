"""
【闭包】
指的是在一个函数内部定义另一个函数，并且内部函数引用了外部函数的变量，同时外部函数的返回值是内部函数的引用
作用：用于实现装饰器、用于保存状态信息、用于实现函数时编程
"""


def outer_function(x):
    # 1. 定义一个内部函数
    def inner_function(y):
        # 2. 内部函数可以引用外部函数的变量
        return x + y
    # 3. 返回值是内部函数的引用
    return inner_function


# 创建闭包
closure = outer_function(10)

# 使用闭包
result = closure(5)
print(result)  # 输出 15
