import random

"""
random 模块演示
"""

print(f'生成一个 [0.0, 1.0) 之间的随机小数：{random.random()}')

print('\n----------- 设置随机数种子，每次产生的随机数序列相同 -----------')
print('随机数种子设置为 7, 生成 3 次随机数：')
random.seed(7)
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print('随机数种子设置为 7, 生成 3 次随机数：')
random.seed(7)
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

print('\n----------- 随机数常见的几种用法 -----------')
print(f'随机整数 ---- {random.randint(0, 2)}')
print(f'随机小数 ---- {random.randint(0, 2)}')

print('\n----------- 给定一个序列，生成随机数 -----------')
seq = [1, 2, 3, 4]
print(random.choice(seq))
print(random.choice(seq))
print(random.choice(seq))
print(random.choice(seq))
print(random.choice(seq))

print('\n----------- 将一个指定序列进行随机排列 -----------')
random.shuffle(seq)
print(seq)
