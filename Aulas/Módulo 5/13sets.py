# set: é uma estrutura de dados não ordenada e sem duplicidade.

# criando Set:
conjunto1 = set([9, 8, 3, 4, 5, 6])
conjunto2 = {9, 10, 5, 6, 7, 8}
print(conjunto1)
print(conjunto2)
# Convertendo para Set:
set_conjunto2 = set(conjunto2)

conjunto1.add("a")
print(conjunto1)
conjunto2.remove(10)
print(conjunto2)

# conjuntos

uniao = conjunto1.union(conjunto2)  # União
print(uniao)

intersecao = conjunto1.intersection(conjunto2)  # Interseção
print(intersecao)

diferenca = conjunto1.difference(conjunto2)  # diferença
print(diferenca)
