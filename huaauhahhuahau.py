# Huaauhahhuahau | bee 2242

risada = input()
vogais = 'aeiou'
aux = ''

for letra in risada:
    if letra in vogais:
        aux += letra

if aux == aux[::-1]:
    print('S')
else:
    print('N')
