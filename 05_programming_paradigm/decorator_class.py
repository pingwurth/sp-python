"""
【类的常用装饰器】
@classmethod
@staticmethod
@property
"""


class Test(object):
    def __init__(self, name):
        self.__name = name

    def run(self):
        print('run...')
        self.play()
        self.sleep()

    # 入参 cls 是必须的，代表类本身
    @classmethod
    def play(cls):
        print('play...')

    # 不允许传递 self 和 cls 参数，内部无法调用其他类函数和类变量
    @staticmethod
    def sleep():
        print('sleep...')

    # 函数被绑定为属性，可通过 .方法名 调用，不需要括号
    @property
    def name(self):
        return self.__name

    # 必须和 @property 搭配使用
    @name.setter
    def name(self, value):
        self.__name = value


t1 = Test('54pig')
t1.run()

print('\n----------- @classmethod >>>> 装饰的方法可以直接通过类名调用 -----------')
Test.play()

print('\n----------- @staticmethod >>>> 装饰的方法可以直接通过类名调用 -----------')
Test.sleep()

print('\n----------- @property >>>> 方法调用可以省略括号 -----------')
print(t1.name)  # 原本是 t1.name(), 在 @property 的作用下 t1.name 即可

print('\n----------- 修改私有变量 -----------')
t1.name = 'sup bro'
print(t1.name)
