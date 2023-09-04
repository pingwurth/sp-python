"""
【冒泡排序】
- 取第 1 个元素和第 2 个元素进行比较，把较大的数放后面
- 继续比较第 2 个元素和第 3 个元素，重复操作，直到最后一个元素
- 一轮遍历结束，最大值已被移动到最后，继续下一轮...
"""


def buble_sorting(L):
    end = len(L)
    while 0 < end:
        for j in range(0, end):
            if j + 1 < end and L[j] > L[j + 1]:
                L[j] = L[j] ^ L[j + 1]
                L[j + 1] = L[j] ^ L[j + 1]
                L[j] = L[j] ^ L[j + 1]
        end = end - 1


L = [3, 6, 4, 7, 24, 634, 23, 5]
buble_sorting(L)
print(L)
