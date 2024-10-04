# bee 2312 | Quadro de Medalhas

from functools import cmp_to_key


def cmp(pais1, pais2):
    if int(pais1[1]) > int(pais2[1]):
        return -1
    elif int(pais1[1]) < int(pais2[1]):
        return 1
    elif int(pais1[2]) > int(pais2[2]):
        return -1
    elif int(pais1[2]) < int(pais2[2]):
        return 1
    elif int(pais1[3]) > int(pais2[3]):
        return -1
    elif int(pais1[3]) < int(pais2[3]):
        return 1
    elif pais1[0] < pais2[0]:
        return -1
    elif pais1[0] > pais2[0]:
        return 1
    else:
        return 0


n = int(input())
lista = []

while n > 0:
    lista.append(input().split())
    n -= 1

lista.sort(key=cmp_to_key(cmp))

for linha in lista:
    print(linha[0], linha[1], linha[2], linha[3])
