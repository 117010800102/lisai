from random import*
p=randint(0,100)
count=0;
while True:
    n=eval (input("0-100的整数:"))
    count +=1
    if n>p:
        print("太大了")
    elif n==p:
        print("预测了{}次，你猜中了".format(count))
        break
    else:
        print("太小了")
