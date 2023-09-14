import math
import os
import sys

print(math.fabs(-123.0))

"""
os 模块演示
"""

print('\n----------- os 模块 - 实现文件拷贝 -----------')


def copy(source_path, target_path):
    """
    文件内容拷贝，将 source_path 中的内容拷贝到 target_path 中
    :param source_path: 源文件
    :param target_path:
    :return:
    """
    source_fd = os.open(source_path, os.O_RDONLY)
    target_fd = os.open(target_path, os.O_WRONLY | os.O_CREAT)

    while True:
        binary = os.read(source_fd, 512)
        if len(binary) == 0:
            return
        os.write(target_fd, binary)


tmpdir = "/tmp/python/"
copy(tmpdir + "demo.txt", tmpdir + "demo.bak")
print(tmpdir + ' 目录下的文件：')
print(os.listdir(tmpdir))

print('\n----------- os 模块 - 目录切换 & 创建目录 & 获取当前所在目录 & 当前目录下的文件 -----------')
os.chdir('C:\\')

if not os.path.exists('tmp'):
    os.mkdir('tmp')

print(os.getcwd())
print(os.listdir(os.getcwd()))

print('\n----------- os 模块 - 提取 path 中的文件名 -----------')
print(os.path.basename(tmpdir + 'demo.txt'))
print('\n----------- os 模块 - 提取 path 中的目录 -----------')
print(os.path.dirname(tmpdir + 'demo.txt'))
print('\n----------- os 模块 - 文件路径分隔符 -----------')
# Linux 为 /, Windows 为 \
print(os.sep)
print('\n----------- os 模块 - 连接多个参数形成路径 -----------')
new_path = os.path.join('C:\\tmp', 'python', 'test', 'README.md')
print(new_path)
print('\n----------- os 模块 - 判断 path 是否存在 -----------')
print(os.path.exists(new_path))
print('\n----------- os 模块 - 判断 path 是普通文件还是目录文件 -----------')
print(os.path.isdir(new_path))
print(os.path.isfile(new_path))

print('\n----------- os 模块 - 递归列出子目录 -----------')


def list_dir(directory):
    """
    递归列出子目录
    :param directory: 根目录
    :return:
    """
    entries = os.listdir(directory)
    for entry in entries:
        path = os.path.join(directory, entry)
        print(path)
        if os.path.isdir(path):
            list_dir(path)


list_dir('tmp')





"""
sys 模块演示
"""

print('\n----------- sys 模块 - 退出程序 -----------')
# 0 表示正常退出，其他值表示异常退出
sys.exit(0)
