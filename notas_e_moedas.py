# -*- coding: utf-8 -*-

valor = float(input())
valor = int(valor * 100)

n100 = 0
n050 = 0
n020 = 0
n010 = 0
n005 = 0
n002 = 0

m1_00 = 0
m0_50 = 0
m0_25 = 0
m0_10 = 0
m0_05 = 0
m0_01 = 0

while valor >= 10000:
    valor -= 10000
    n100 += 1

while valor >= 5000:
    valor -= 5000
    n050 += 1

while valor >= 2000:
    valor -= 2000
    n020 += 1

while valor >= 1000:
    valor -= 1000
    n010 += 1

while valor >= 500:
    valor -= 500
    n005 += 1

while valor >= 200:
    valor -= 200
    n002 += 1


while valor >= 100:
    valor -= 100
    m1_00 += 1

while valor >= 50:
    valor -= 50
    m0_50 += 1

while valor >= 25:
    valor -= 25
    m0_25 += 1

while valor >= 10:
    valor -= 10
    m0_10 += 1

while valor >= 5:
    valor -= 5
    m0_05 += 1

while valor >= 1:
    valor -= 1
    m0_01 += 1

print(f'NOTAS:\n{n100} nota(s) de R$ 100.00\n{n050} nota(s) de R$ 50.00\n{n020} nota(s) de R$ 20.00\n{n010} nota(s) de R$ 10.00\n{n005} nota(s) de R$ 5.00\n{n002} nota(s) de R$ 2.00')
print(f'MOEDAS:\n{m1_00} moeda(s) de R$ 1.00\n{m0_50} moeda(s) de R$ 0.50\n{m0_25} moeda(s) de R$ 0.25\n{m0_10} moeda(s) de R$ 0.10\n{m0_05} moeda(s) de R$ 0.05\n{m0_01} moeda(s) de R$ 0.01')
