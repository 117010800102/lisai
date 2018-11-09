def isprime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
while True:
    try:
        n=eval(input("Enter an integar:"))
    except:
        print("Enter error !please enter again:")
        continue
    if type(n) is not int:
        print("please enter an integar:")
        continue
    if n == -1:
        break
    if isprime(n):
        print("{} is prime".format(n))
    else:
        print("{} is not prime".format(n))
