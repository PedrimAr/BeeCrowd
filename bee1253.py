# Cifra de César | bee 1253

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n = int(input())

while n > 0:
    codificada = input()
    descodificada = ''
    pulo = int(input())
    indice_desc = 0

    for i in range(len(codificada)):
        if alfabeto.index(codificada[i]) - pulo < 0:
            descodificada += alfabeto[alfabeto.index(codificada[i]) - pulo + 26]
        else:
            descodificada += alfabeto[alfabeto.index(codificada[i]) - pulo]

    print(descodificada)
    n -= 1
