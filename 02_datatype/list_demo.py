"""
【列表】
- 官方文档：https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- 中文文档：https://www.apiref.com/python-zh/tutorial/datastructures.html#more-on-lists

| 常用的列表函数               | 功能描述                                     |
| ------------------------- | ------------------------------------------ |
| len(L)                    | 获取列表的长度                                |
| max(L)                    | 获取列表中的最大元素                           |
| min(L)                    | 获取列表中的最小元素                           |
| L.append(item)            | 向列表中新增一个元素 item                      |
| L.insert(index, item)     | 将元素 item 插入列表指定位置 index             |
| L.pop() / L.pop(n)        | 从列表尾部取出一个元素 / 取出指定位置 n 的元素    |
| L.remove(item)            | 从列表中删除指定元素 item                     |
| L.index(item)             | 在列表中查找指定元素 item，如果找到返回其索引     |
| L.reverse()               | 将列表中元素倒序排列                          |
| L.sort()                  | 对列表中的元素进行排序                        |
"""

print('\n----------- 定义一个 list 并直接打印输出 -----------')
# 定义一个 list
scores = [45, 60, 75,86, 49, 100]
# 什么类型都可以放到同一个 list 中
L = ['Alice', 66, 'Bob', True, 'False', 100]
# 直接打印输出 list
print(L)

print('\n----------- 用 for 循环输出 list 中每一项 -----------')
L = ['Alice', 66, 'Bob', True, 'False', 100]
for item in L:
    print(item)

print('\n----------- 用索引访问 list 中每一项 -----------')
for index in range(0, 6):
    print(L[index])

print('\n----------- 切片方式获取 list 子列表 -----------')
print(L[0:2])

print('\n----------- 倒序访问 list 中的元素 -----------')
print(L[-1])

print('\n----------- list - 添加元素: append 和 insert -----------')
classmates = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
print('原始 list - ', classmates)
classmates.append('Zero')
print('追加了一个元素后 - ', classmates)
classmates.insert(5, 'Phoebe')
classmates.insert(5, 'Gen')
print('又插入两个元素 - ', classmates)

print('\n----------- list - 删除元素: pop、pop(n) -----------')
L = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
L.pop()
# 删除指定位置的元素
L.pop(2)
print(L)

print('\n----------- list - 替换元素 -----------')
L = ['Alice', 'Bob', 'Candy', 'David']
print('替换前 - ', L)
L[2] = '54pig'
print('替换后 - ', L)

print('\n----------- 二维 list -----------')
alice_scores = [100, 89, 92]
bob_scores = [70, 65, 81]
candy_scores = [88, 72, 77]
all_scores = [alice_scores, bob_scores, candy_scores]
print(all_scores)

print('\n----------- 二维 list 示例: 计算 3 个长方体的表面积 -----------')
L = [[1, 2, 3], [5, 3, 2], [7, 3, 2]]
print('3 个长方体的长宽高 - ', L)
# 使用 enumerate 函数可以同时列举索引和值
for index, cube in enumerate(L, 1):
    length = cube[0]
    width = cube[1]
    height = cube[2]
    surface_area = length * width * height
    print(f'第 {index} 个长方体的表面积 = {surface_area}')
