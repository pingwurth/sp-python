"""
【集合】
无序的、不允许重复元素
"""

print('\n----------- 创建一个 set, 注意和 list 的区别 -----------')
s = {1, 4, 3, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6}
print('a set - ', s)
L = [1, 2, 3, 4, 6, 6, 6]
print('a list - ', L)

print('\n----------- 读取 set -----------')
for item in s:
    print(item)

print('\n----------- 添加 set - add 和 update -----------')
names = {'Alice', 'Bob', 'Candy', 'David', 'Ellena'}
names.add('pppp')
names.update({'54pig', '54pink', '54ppppp'})
print(names)

print('\n----------- 删除 set 元素 - remove() -----------')
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S = {1, 3, 5, 7, 9}
for item in L:
    if item in S:
        S.remove(item)
    else:
        S.add(item)
print(S)

print('\n----------- 删除 set 元素（元素不存在也不会报错） - discard() -----------')
names = {'Alice', 'Bob', 'Candy', 'David', 'Ellena'}
names.discard('fj4i23qu5o32hr')
print(names)

print('\n----------- 清理 set - clear() -----------')
names.clear()
print(names)

print('\n----------- 子集、超集、重合 -----------')
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('s1 是 s2 的子集（s1 的元素全部存在于 s2 中）：', s1.issubset(s2))
print('s2 是 s1 的超集（s2 包含了 s1 的所有元素）：', s2.issuperset(s1))
print('s1 和 s2 中有重复元素：', not s1.isdisjoint(s2))
