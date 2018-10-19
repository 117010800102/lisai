# 判断素数
n = int(input("输入一个正整数："))
f = 1
for i in range(2,n):
    if n%i == 0:
        f = 0
        break
if f == 1:
    print("{}是素数".format(n))
else:
    print("{}不是素数".format(n))
