from random import*
N=1000000
sequence=["车","羊1","羊2"]
first_guess_count = 0
change_guess_count = 0
for i in range(N):
    guess=choice(sequence)
    if guess =="车":
        first_guess_count += 1
    else:
        change_guess_count += 1
print("改变获胜的概率:{:.4f};坚持获胜的概率:{:.4f}".format(first_guess_count/N,change_guess_count/N))
