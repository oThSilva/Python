# nomes = ["Zack", "Camila", "Julius", "Romer"]
# valores = [9, 1, 7, 3, 8, 4, 6, 2, 5, 0]
# print(nomes)
# print(valores)
# nomes.sort()
# valores.sort()
# print(nomes)
# print(valores)

# # biblioteca para ordenar valores que tenham chaves ou propriedades

from operator import itemgetter

# pessoas = [
#     {"nome": "Jonh", "Idade": 32, "Nivel de acesso": 2},
#     {"nome": "Carol", "Idade": 18, "Nivel de acesso": 3},
#     {"nome": "Tomas", "Idade": 45, "Nivel de acesso": 5},
#     {"nome": "Amanda", "Idade": 23, "Nivel de acesso": 1},
# ]
# pessoas.sort(key=itemgetter("nome"))
# print(pessoas)

# # uma lista com tuplas
# produtos = [
#     ("Celular", 7500),
#     ("Bicicleta", 8500),
#     ("Microfone", 150),
# ]
# produtos.sort(key=itemgetter(1))  # 1 é o indice
# print(produtos)
# # Ordenar de forma invertida
# produtos.sort(key=itemgetter(1), reverse=True)
# print(produtos)

# matriz = [[5, 10], [15, 21], [1, 5]]
# matriz.sort(key=itemgetter(1))
# print(matriz)


# Ordene a lista de produtos abaixo pelo preço em ordem crescente
produtos = [
    {"nome": "Celular", "preco": 1500},
    {"nome": "Monitor", "preco": 500},
    {"nome": "Microfone", "preco": 300},
]
produtos.sort(key=itemgetter("preco"))
print(produtos)

#  Ordene em ordem descrescente a lista de equipamento_filmagem por valor do equipamento

equipamento_filmagem = [
    ("Tripé", 300),
    ("Câmera", 1700),
    ("Iluminação", 200),
]
equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)
#  Ordene em ordem crescente a cotacao_moedas com base no valor da moeda

cotacao_moedas = [["usd", 5.25], ["brl", 1.56], ["eur", 6.47]]
cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)
