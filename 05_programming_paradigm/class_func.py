class CallableClass:
    def __call__(self, *args, **kwargs):
        print("对象被调用了！")
        # 在这里添加你希望对象被调用时执行的代码


# 创建一个可调用的对象
obj = CallableClass()

# 调用对象，会触发 __call__ 方法的执行
obj()
