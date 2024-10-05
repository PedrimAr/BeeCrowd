# bee 2415 | Consecutivos

n = int(input())
sorteados = list(map(int, input().split()))
sorteados.append(10000000000000000000000000000000000000000000000000000000000000)
sequencia_atual = 1
maior_sequencia = 0

for i in range(n):
    if sorteados[i + 1] == sorteados[i]:
        sequencia_atual += 1
    else:
        if sequencia_atual > maior_sequencia:
            maior_sequencia = sequencia_atual

        sequencia_atual = 1

print(maior_sequencia)
