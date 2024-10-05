# Encaixa ou não II | bee 1241

n = int(input())

while n > 0:
    a, b = input().split()

    if len(a) >= len(b):
        if a[len(a) - len(b):] == b:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")

    n -= 1
