import os
import sys

"""
模块示例
"""

print('\n----------- 列出对象的属性 -----------')
print(dir(sys))

print('\n----------- 查看对象的帮助文档 -----------')
help(sys)
help(os.open)


def get_project_dir():
    # 获取当前脚本的绝对路径
    script_path = os.path.abspath(__file__)
    # 获取当前脚本所在的目录
    script_dir = os.path.dirname(script_path)
    # 获取当前项目的目录
    project_dir = os.path.dirname(script_dir)
    return project_dir
