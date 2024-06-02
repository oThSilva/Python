# Trabalhando com Multiuplas listas
a_lista = ["A", "B", "C", "D", "E"]
b_lista = [1, 2, 3, 4, 5]

for a, b in zip(a_lista, b_lista):
    print(a)
    print(b)

produtos = ["Produto 1 ", "Produto 2 ", "Produto 3"]
preco = [100, 200, 300]
for a, b in zip(produtos, preco):
    print(f"Salvando produto {a} valor de {b}")


from itertools import zip_longest

titulos = ["titulo 1 ", "titulo 2", "titulo 3", "titulo 4"]
descricoes = ["descrição 1", "descrição 2", "descrição 3"]
for titulo, descrecao in zip_longest(titulos, descricoes):
    print(f"Encontramos o {titulo} descrição {descrecao}\n")

produtos = ["Produto 1 ", "Produto 2 ", "Produto 3", "Produto 4", "Produto 5"]
preco = ["R$ 100", "R$ 200", "R$ 300", "R$ 400"]
for a, b in zip_longest(produtos, preco):
    print(f"Produto: {a} encontrado no valor de {b}")
