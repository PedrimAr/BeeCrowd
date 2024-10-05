# Soma de Frações | bee 2443

'''
def mmc(b, d):
    if d > b:
        b, d = d, b
    denominador = 0
    i = 1
    while denominador == 0:
        if (b * i) % d == 0:
            denominador = b * i
        i += 1
    return denominador


def mdc(n, m):
    if n > m:
        n, m = m, n
mdc = 0
j = 1
while mdc == 0:
    if denominador % (numerador / j) == 0:
        mdc = numerador / j
    j += 1
    return mdc


def soma(denominador, a, b, c, d):
    a, c = a * (denominador / b), c * (denominador / d)
    numerador = a + c
    return numerador


def reducao(numerador, denominador):
    numerador, denominador = int(numerador / mdc(numerador, denominador)), int(denominador / mdc(numerador, denominador))
    print(f'{numerador} {denominador}')


a, b, c, d = map(int, input().split())
reducao(soma(mmc(b, d), a, b, c, d), mmc(b, d))
'''

a, b, c, d = map(int, input().split())
''
if d > b:
    b, d = d, b
    a, c = c, a

denominador = 0
i = 1

while denominador == 0:
    if (b * i) % d == 0:
        denominador = b * i
    i += 1

a, c = a * (denominador // b), c * (denominador // d)
numerador = a + c

mdc = 0
j = 1


while mdc == 0:
    if denominador % (numerador / j) == 0:
        mdc = numerador / j
    j += 1
numerador = int(numerador / mdc)
denominador = int(denominador / mdc)


print(f'{numerador} {denominador}')
