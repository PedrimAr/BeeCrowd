# -*- coding: utf-8 -*-

codigo, quantidade = input(). split()
codigo = int(codigo)
quantidade = int(quantidade)
valor = 0
if codigo == 1:
    valor = quantidade * 4
elif codigo == 2:
    valor = quantidade * 4.5
elif codigo == 3:
    valor = quantidade * 5
elif codigo == 4:
    valor = quantidade * 2
elif codigo == 5:
    valor = quantidade * 1.5
print(f'Total: R$ {valor:.2f}')
