# bee 2293 | Campo de Minhocas

n, m = map(int, input().split())
matriz = []
maior_soma = 0


for i in range(n):
    linha = [0] * n
    linha[:] = map(int, input().split())
    matriz.append(linha[:])

for j in range(n):
    soma = 0
    for k in range(m):
        soma += matriz[j][k]
    if soma > maior_soma:
        maior_soma = soma

for l in range(m):
    soma = 0
    for o in range(n):
        soma += matriz[o][l]
    if soma > maior_soma:
        maior_soma = soma

print(maior_soma)
