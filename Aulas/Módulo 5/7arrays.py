# array

from array import array

# array("código de tipo",[valores do array])

numeros = array("i", [1, 2, 3, 4, 5, 6, 7])
print(numeros)
numeros.append(8)  # para add um item no fim do array
print(numeros)
numeros.insert(0, 0)  # para inserir um item em um index especifico
print(numeros)
numeros.pop(0)  # para excluir um valor pelo index
print(numeros)
numeros.remove(7)  # para remover um valor usando o valor
print(numeros)
del numeros[1]  # para deletar pelo index ou faixa de index
print(numeros)
