# Cartas | bee 2456

cartas = input().split()
crescente = True
decrescente = True

for i in range(len(cartas) - 1):
    if int(cartas[i]) > int(cartas[i + 1]):
        crescente = False
    else:
        decrescente = False

if crescente:
    print('C')
elif decrescente:
    print('D')
else:
    print('N')
