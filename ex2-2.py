#yuan change to dollor
Money=input("带符号的金钱数目:")
if Money[-1] in ["y","Y"]:
    M=6*eval(Money[:-1])
    print("兑换后的金钱是{:.2f}D:".format(M))
elif Money[-1] in ["d","D"]:
    M=eval(Money[:-1])/6
    print("兑换后的金钱是{:.2f}F".format(M))
else:
    print("输入格式错误:")
