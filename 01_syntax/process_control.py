"""
流程控制：分支结构
"""
print('\n----------- 条件分支 if 语句 -----------')
score = 59
if score < 60:
    print('抱歉，考试不及格')

print('\n----------- 条件分支 if-else 语句 -----------')
score = 60
if score < 60:
    print('抱歉，考试不及格')
else:
    print('恭喜你，考试及格')

print('\n----------- 条件分支 if-elif-else 语句 -----------')
score = 90
if score < 60:
    print('抱歉，考试不及格')
elif score >= 90:
    print('恭喜你，拿到卓越的成绩')
elif score >= 80:
    print('恭喜你，拿到优秀的成绩')
else:
    print('恭喜你，考试及格')

"""
流程控制：循环结构
"""
print('\n----------- for 循环：求几位同学的平均分 -----------')
L = [75, 92, 59, 68, 99]
sum = 0
for score in L:
    sum += score
average = sum / len(L)
print(average)

print('\n----------- while 循环：求 1~10 的乘积 -----------')
num = 1
result = 1
while num <= 10:  # <<<
    result *= num  # ^
    num += 1  # >>>>>>^
print(result)

print('\n----------- break 使用：计算 0~1000 所有偶数和 -----------')
sum = 0
num = 0
while True:
    num += 2
    if num > 1000:
        break
    sum += num
print(sum)

print('\n----------- continue 使用：计算 0~1000 所有偶数和 -----------')
sum = 0
num = 0
while num <= 1000:
    num += 1
    if num % 2 != 0:
        continue
    sum += num
print(sum)

print('\n----------- 嵌套循环示例 -----------')
s1 = 'ABC'
s2 = '123'
s3 = 'xyz'
for ch1 in s1:
    for ch2 in s2:
        for ch3 in s3:
            print(ch1 + ch2 + ch3)

