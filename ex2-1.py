TempStr=input("带符号的温度值")
if TempStr [-1] in ["F","f"]:
    c=(eval(TempStr[0:-1])-32)/1.8
    print("华氏温度{}转换为摄氏温度:{:.2f}c".format(TempStr,c))
elif TempStr[-1] in ["C","c"]:
    F=eval(TempStr[0:-1])*1.8+32
    print("摄氏温度{}转换为华氏温度:{:.2f}F".format(TempStr,F))
else:
    print("输入格式错误")
