# bee 1933 | Tri-du

# LEIA a e b
a, b = map(int, input('Informe o valor das duas primeiras cartas, separadas por um espaço: ').split())

# SE a = b OU a > b ENTÃO
if a == b or a > b:
    # c <- a
    c = a
# SENÃO ENTÃO
else:
    # c <- b
    c = b

# IMPRIMA c
print(c)
