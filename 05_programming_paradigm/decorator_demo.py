"""
【装饰器】
也是一种函数，可以接受函数作为参数，可以返回函数；
可以对接收的函数进行增强，可以执行它，也可以不执行；
"""


def decorator(func):
    """
    接受一个函数 func，定义一个内部函数去执行 func
    :param func: 一个函数
    :return: 定义的内部函数
    """

    def inner_function(*args, **kwargs):
        return func(*args, **kwargs)

    return inner_function


def f(s):
    print(s)


print('\n----------- 装饰器示例 -----------')
decorator(f)('ping')  # f 函数先进行装饰，再调用


def check_str(func):
    print('func:', func)

    def inner(*args, **kwargs):
        print('args:', args, kwargs)
        ret = func(*args, **kwargs)
        if ret == 'ok':
            return 'result is %s' % ret
        else:
            return 'result is failed:%s' % ret

    return inner


print('\n----------- 用 @ 实现装饰器 -----------')


@check_str
def test(data):
    return data


print(test(data='ok'))
