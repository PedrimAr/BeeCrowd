# Máquina de Café | bee 2670

lista = [int(input()) for i in range(3)]
tempo_gasto = [lista[0] * 4 + lista[1] * 2, lista[0] * 2 + lista[2] * 2, lista[1] * 2 + lista[2] * 4]

tempo_gasto.sort()
print(tempo_gasto[0])
