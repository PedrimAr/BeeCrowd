# bee 1940 | Jogo da Estratégia

j, r = map(int, input().split())
pontos = list(map(int, input().split()))
soma_atual = 0
maior_soma = 0
vencedor = 0

for i in range(j):
    for k in range(i, len(pontos), j):
        soma_atual += pontos[k]

    if soma_atual >= maior_soma:
        maior_soma = soma_atual
        vencedor = i + 1

    soma_atual = 0

print(vencedor)
