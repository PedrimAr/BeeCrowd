# bee 2187 | Bits Trocados

v = 10001
n = 0
# ENQUANTO v > 0 FAÇA:
while True:
    # LEIA v
    v = int(input())
    if v == 0:
        break
    valor = v
    i, j, k, l = 0, 0, 0, 0

    # ENQUANTO v >= cedula  FAÇA:
        # _ <- _ + 1
        # v <- v - cedula
    while valor >= 50:
        i += 1
        valor -= 50
    while valor >= 10:
        j += 1
        valor -= 10
    while valor >= 5:
        k += 1
        valor -= 5
    while valor >= 1:
        l += 1
        valor -= 1

    # n <- n + 1
    n += 1
    # IMPRIMA "Teste" n
    print(f'Teste {n}')
    # IMPRIMA i, j, k, l
    print(f'{i} {j} {k} {l}')
    # IMPRIMA linha vazia
    print()
