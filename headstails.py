import random


def flip(n):
    f = []
    for i in range(n):
        m = random.randrange(2)
        if m == 0:
            f.append("Heads")
        else:
            f.append("Tails")
    print(f)


n = int(input("How many times do you want to flip the coin?"))
flip(n)
