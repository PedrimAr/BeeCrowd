# bee 2295 | Frota de Táxi

a, g, Ra, Rg, =  map(float, input().split())
Ea = a / Ra
Eg = g / Rg

if Ea < Eg:
    print('A')
else:
    print('G')
