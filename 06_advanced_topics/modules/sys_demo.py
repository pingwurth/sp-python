import sys
import time

"""
sys 模块演示
"""

print('\n----------- sys 模块 - 命令行参数 -----------')
print(sys.argv)  # sys.argv 是一个数组

print('\n----------- sys 模块 - 示例：打印下载进度 -----------')
for rate in range(101):
    text = 'Downloading %d%%' % rate
    sys.stdout.write(text)
    sys.stdout.write('\r')  # 输出 '\r'，将光标移动到行首
    time.sleep(0.01)

print('\n----------- sys 模块 - 系统路径（Python 库的路径列表） -----------')
print(sys.path)

print('\n----------- sys 模块 - 输出 Python 版本、系统版本 -----------')
print(sys.version)
print(sys.platform)

print('\n----------- sys 模块 - 退出程序 -----------')
# 0 表示正常退出，其他值表示异常退出
sys.exit(0)

print('\n----------- sys 模块 - 标准输入、标准输出、标准错误输出 -----------')
line = sys.stdin.readline()
sys.stdout.write(line)
sys.stderr.write(line)
