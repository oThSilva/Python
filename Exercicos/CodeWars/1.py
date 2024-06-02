# Sua tarefa é escrever uma função que usa uma cadeia de caracteres e retornar uma nova cadeia de caracteres com todas as vogais removidas.


def disemvowel(string_):
    vogais = "aeiouAEIOU"
    resultado = "".join(caracter for caracter in string_ if caracter not in vogais)

    return resultado


frase = "Pão com leite"
sem_volga = disemvowel(frase)
print(frase)
print(sem_volga)


# O operador in verifica se um valor está presente em um conjunto, enquanto o operador not in verifica se um valor não está presente em um conjunto (inverte a operação).
# valor {operadores} sequencia
numeros = [1, 2, 3, 4, 5]
resultado = 6 in numeros
print(resultado)
