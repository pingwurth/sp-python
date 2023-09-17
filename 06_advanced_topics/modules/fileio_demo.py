import os
from module_demo import *

"""
文件 io 操作

| 模式  | 描述             | 如果文件存在                 | 如果文件不存在              |
| :--- | :-------------- | :------------------------- | :------------------------ |
| r    | 以只读方式打开文件 | 保留原有内容，从文件头部开始读   | 抛出异常 FileNotFoundError |
| r+   | 以读写方式打开文件 | 保留原有内容，从文件头部开始读   | 抛出异常 FileNotFoundError |
| w    | 以只写方式打开文件 | 删除原有内容，从文件头部开始写入 | 创建新文件                 |
| w+   | 以读写方式打开文件 | 删除原有内容，从文件头部开始读写 | 创建新文件                 |
| a    | 以只写方式打开文件 | 保留原有内容，从文件尾部开始读写 | 创建新文件                 |
| a+   | 以读写方式打开文件 | 保留原有内容，从文件尾部开始读写 | 创建新文件                 |

"""

demo_file = get_project_dir() + os.sep + "demo.txt"

print('\n----------- 打开文件 -----------')
file = open(demo_file, mode='r', encoding='utf-8')

print('\n----------- 读取文件中的数据 - read() 或 readlines() -----------')
s = file.read()
# lines = file.readlines()
print(s)

print('\n----------- 关闭文件 -----------')
file.close()

file = open(demo_file, mode='r+', encoding='utf-8')
print('\n----------- 获取文件当前的访问位置 - tell() -----------')
print(file.tell())

print('\n----------- 改变文件当前的访问位置 seek(offset, from) -----------')
content = file.read()
# 参数 offset 表示要移动的字节数
# 参数 from 指定开始移动字节的参考位置
#   如果 from 被设为 0，将文件的开头作为移动的参考位置
#   如果 from 被设为 1，将文件的当前访问位置作为移动的参考位置
#   如果 from 被设为 2，将文件的末尾作为移动的参考位置
file.seek(len(content) - 10, 0)
print(file.readline())
