# Geradores em Python são funções especiais que permitem criar iteradores de forma fácil e eficiente. Eles são usados para gerar uma sequência de valores de maneira preguiçosa, ou seja, os valores são gerados sob demanda, conforme necessários, em vez de gerar todos os valores de uma vez. Isso os torna ideais para trabalhar com sequências potencialmente grandes ou infinitas.

# Funções geradoras: Geradores são criados usando funções definidas com a palavra-chave yield em vez de return. Quando uma função geradora é chamada, ela retorna um objeto gerador, que pode ser iterado sobre ele.

# Lazy Evaluation: Os valores são gerados conforme necessários, um por vez, em vez de todos de uma vez. Isso permite economizar memória e tempo de processamento, especialmente ao lidar com grandes volumes de dados.

# Estado da função mantido: Quando uma função geradora é pausada após a execução do yield, o estado da função é mantido, permitindo que ela continue de onde parou quando chamada novamente.

# Iteração em loops: Geradores podem ser usados em loops for e outras estruturas de controle que suportam iteração.


def gerar_pares(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


# Criando um gerador
gerador = gerar_pares(20)

# Iterando sobre os valores gerados
for numero in gerador:
    print(numero)


def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for i in meu_gerador(numeros=[1, 2, 3, 4, 5]):
    print(i)
