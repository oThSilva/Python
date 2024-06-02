# lista []
precos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(precos[0])  # para acessar o valor do indice
print(precos[precos.index(100)])
# listas são dinâmicas
itens = [1, "Olá", True, 10.99]
print(itens)
# Multiplicação de valores
lista_de_oitos = [8] * 10
lista_de_texto = ["Th"] * 5
print(lista_de_oitos)
print(lista_de_texto)
# Usando o gerador range(Sequência) 1 até 30
faixa_de_numeros = list(range(1, 31))
print(faixa_de_numeros)
# gerar lista a partir de strings
print(list("Th produções"))
# lista de lista(matriz)
matriz_de_nomes = [["Thiago", 24], ["Giovanna", 22]]
print(matriz_de_nomes[0])
print(matriz_de_nomes[0][0])
print(matriz_de_nomes[1][0])

# Compreensão de listas

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = [x**2 for x in numeros]
print(quadrados)

numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados_pares = [x**2 for x in numeros if x % 2 == 0]
print(quadrados_pares)

# Desafio 1:
lista_objetos = ["Celular", "Fone", "Alicate"]
print(lista_objetos)

# Desafio 2:
contador = list(range(10, 132))
print(contador)

# Desafio 3:
print(lista_objetos + contador)

# Desafio 4:
matriz_de_objetos = [
    [lista_objetos[0], "R$ 2500"],
    [lista_objetos[1], "R$ 300"],
    [lista_objetos[2], "R$ 60"],
]
print(matriz_de_objetos)
