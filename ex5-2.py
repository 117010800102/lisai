def isodd(n):
    if n%2 ==1:
        return True
    else:
        return False
while True:
    s = input("")
    if not s.isdigit():
        print("")
        countinue
    n = eval (s)
    if n == -1:
        print("program is over!")
        break
    if isodd(n):
        print("{} is odd".format(n))
    else:
        print("{} is even".format (n))
