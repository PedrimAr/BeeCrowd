# bee 3048 | Sequência Secreta

n = int(input())
sequencia = []
marcados = 1

for i in range(n):
    sequencia.append(int(input()))

for i in range(n - 1):
    if sequencia[i] != sequencia[i + 1]:
        marcados += 1

print(marcados)
