"""
【面向对象】
构造函数
私有变量、私有函数
装饰器
继承与多态
"""


class Person(object):
    """
    定义一个 Person 类
    """

    # 私有变量（以双下划线开头）
    __assets = 3489578935.32

    def __init__(self, name, age=None):
        """
        类的构造函数
        :param name: 名字
        :param age: 年龄
        """
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} 在奔跑')

    def __descript(self):
        """
        私有函数，以 __ 开头
        :return:
        """
        print(f'{self.name} has {self.__assets} asset')


# 类的实例化：创建一个 Person 对象
ping = Person('54pig', 31)
ping.run()

# self 是类函数中的必传参数，且必须放在第一个参数位置
# self 是一个对象，他代表实例化的变量自身
# self 可以直接通过点来定义一个类变量：self.name = 'ping'
# self 中的变量与含有 self 参数的函数可以在类中的任何一个函数内随意调用
