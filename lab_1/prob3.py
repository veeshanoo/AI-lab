import random


def game(x):
    nr = random.randint(0, 10)

    for i in range(0, x):
        s = int(input("dati un numar\n"))
        if s == nr:
            print("ati ghicit numarul")
            return

        if s < nr:
            print("numarul dat este mai mic")
            continue

        print("numarul dat este mai mare")

    print("nu ati ghicit numarul")

game(10)
