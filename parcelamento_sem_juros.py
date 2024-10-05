# bee 3060 | Parcelamento Sem Juros

v = int(input())
p = int(input())

if v % p != 0:
    for i in range(v % p):
        print(int(v / p) + 1)

for i in range(p - (v % p)):
    print(int(v / p))
