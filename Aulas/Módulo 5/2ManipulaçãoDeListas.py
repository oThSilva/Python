valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# para copiar uma lista
valores2 = valores.copy()

print(valores)
valores.append(11)  # Para add um item no final da lsita
print(valores)
anos = [2020, 2021, 2022, 2023]
# Unir listas
valores.extend(anos)
print(valores)
# add lista
nova_lista = valores + anos
print(nova_lista)
# acessar um indice de uma lista
print(anos[1])
# inserir um item em uma lista
anos.insert(2, 2022)  # (index, valor)
print(anos)
# extrair com base no indice
ano_2020 = anos.pop(0)
print(ano_2020)
# remover item da lista
anos.remove(2022)  # remover por valor
del valores[0]  # remover por indice
del valores[0:3]  # remover por faixa de indices
# contando a ocorrência de um valor
print(anos.count(2020))
# limpar os valores dentro de uma lista
valores.clear()
