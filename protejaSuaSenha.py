'''

beecrowd | 2287
PROTEJA SUA SENHA

Etapa 1: Compreender o problema
    Sobre o que é o problema?
        Tentativa de identificação de senhas codificadas
    Dados de entrada:
        Número de associações (N);
        10 números, em ordem de associação para as 5 letras;
        6 letras, que representam a senha codificada.
    Regras do jogo
    A senha composta por 6 dígitos, de 0 a 9, é digitada por
    meio de 5 letras, de A a E, as quais representam,
    cada uma, 2 números aleatórios;
    A alocação dos números para cada letra sempre alterna;
    A descodificação sempre sera possível com as N associações
    fornecidas.
    Saída esperada:
        Teste 1
        Senha descodificada, com números separados por 1 espaço
        .
        .
        .
        Teste n
        Senha descodificada, com números separados por 1 espaço
'''

# Etapa 2: Algoritmo

# Ler o número N de observações
N = int(input())

# Enquanto N != 0 faça
while N != 0:

    # --> Na primeira observação
    # Ler os pares de números e associá-los a cada letra
    linha = input().split()
    numeros = map(int, linha[:11])
    # Para cada numero, pulando de 2 em 2
        # Adicionar numero e sucessor à lista de cada letra

    senhaCodificada = map(int, linha[11:])
    
    # Para cada "casinha" da minha senha (são 6)
    for letra in senhaCodificada:
        # Ler a letra que o usuário informou
        # Pegar o par de números associado a essa letra
        # Colocar esse par de números como candidatos à dígito numérico da "casinha" atual

    # --> Para cada outra das observações faça
        # Ler os pares de números e associá-los a cada letra
        # Para cada "casinha" da minha senha (são 6)
        # Ler a letra que o usuário informou
        # Pegar o par de números associado a essa letra
        # Manter na casinha atual o ou os números que se repetiram no par de números associados a ela atualmente

    # Mostrar, para cada casinha da senha, o único número que persistiu

    # Ler o número N de observações
