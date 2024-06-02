# Criar listas usando loops e range
numeros = []
for numero in range(6):
    numeros.append(numero)
print(numeros)

# Para aplicar uma função para cada item de uma lista
# Map
nomes = ["Larissa", "Rafael", "Marcos", "Jonh"]


def aprovar_pessoa(nome):
    return nome + " Aprovado"


print(list(map(aprovar_pessoa, nomes)))
