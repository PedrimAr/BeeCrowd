# bee 1549 | FIla do Recreio

n = int(input())

while n > 0:
    m = int(input())
    fila = input().split()
    fila_2 = sorted(fila, key=int, reverse=True)
    aux = 0

    for i in range(m):
        if int(fila[i]) == int(fila_2[i]):
            aux += 1

    print(aux)
    n -= 1
