# Python 学习


##  Python 安装

**1. 下载安装包**

官网下载：https://www.python.org/downloads/

Python 3.8.10：https://www.python.org/ftp/python/3.8.10/python-3.8.10-embed-amd64.zip

国内镜像源：https://mirrors.huaweicloud.com/python/

**2. 解压安装包**

```cmd
# 解压到 C:\devops\Python38 目录下
C:\Users\59411\Downloads>7z x python-3.8.10-embed-amd64.zip -o"C:\devops\Python38"
```

**3. 验证安装是否成功**

```cmd
# 1. 进入安装目录
C:\Users\59411\Downloads>cd C:\devops\Python38
# 2. 查看 Python 版本号
C:\devops\Python38>python --version
Python 3.8.10 # 正常显示版本号表示安装成功
```

**4. 添加环境变量**

快捷键 `Win + R` -> 打开：`sysdm.cpl` -> 高级 -> 环境变量

​	找到`系统变量`Path，编辑 -> 新建 -> 输入 Pyton 安装目录 `C:\devops\Python38`

<font color=blue>注意：如果 Path 变量中设置了其他 Python 版本的路径，需要把当前要设置的放在最前面才会生效。</font>

**5. 验证环境变量是否生效**

```cmd
# 在任意目录下执行 python 命令，进入 python 交互模式
C:\Users\59411>python
Python 3.8.10 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> "hello python"
'hello python'
>>> ^Z  # Ctrl + Z 退出交互模式
```

### 其他必装工具包

> **pip**
>
> - https://pip.pypa.io/en/stable/installation/
>
> **pipenv**
>
> - https://github.com/pypa/pipenv
>
> - https://pipenv.pypa.io/en/latest/

