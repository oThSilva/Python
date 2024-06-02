# Dicionario {Chave:valor}
dicionario_pessoa = {"Nome: ": "Th", "Idade: ": "18", "Altura: ": "1.70"}
print(dicionario_pessoa)
# outra maneira de criar dicionario

dicionario_2 = dict(nome="Th", Idade="24", altura="1.70")
print(dicionario_2)

# O método setdefault() em Python é usado para retornar o valor associado a uma chave em um dicionário. Se a chave não existir, o método insere a chave com o valor padrão especificado e retorna esse valor

dicionario_2.setdefault("telefone", "3215-2156")
print(dicionario_2)


# O método update() em Python é usado para atualizar um dicionário com os pares chave-valor de outro dicionário ou de uma sequência de pares chave-valor (como uma lista de tuplas). Se a chave existir no dicionário original, o valor correspondente será substituído pelo novo valor. Se a chave não existir, um novo par chave-valor será adicionado ao dicionário original.

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"b": 3, "c": 4}

dicionario1.update(dicionario2)
print(dicionario1)

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"b": 3, "c": 4}

dicionario1.update(dicionario2)
print("Update", dicionario1)


# para copiar um dicionario

copia = dicionario_pessoa.copy()
copia = {"nome": "Th"}
print(copia)

# fromkeys() em Python é usado para criar um novo dicionário a partir de uma sequência (como uma lista, tupla, etc.), onde cada elemento da sequência se torna uma chave no novo dicionário
dicionario_pessoa2 = dict.fromkeys(["Idade"], "15")
print(dicionario_pessoa2)

# O método get() em Python é usado para recuperar o valor associado a uma chave em um dicionário. Ele permite acessar um valor de forma segura, sem gerar um erro se a chave não existir no dicionário

valor = dicionario_pessoa2.get("altura")
print(valor)

# para acessar o valor de uma chave especifica
print(dicionario_pessoa["Altura: "])


# para ver todas as chaves de um dicionario
print(dicionario_pessoa.keys())

# Para ver se a chave pertence ao dicionario

resultado = "Nome" in dicionario_2
print("In", resultado)

# para ver todos os valores de um dicionario
print(dicionario_pessoa.values())

# Para retornar em uma tupla dentro de uma lista as chaves e os valores de um dicionario
print(dicionario_pessoa.items())

# Iterar sobre um dicionarios

for item in dicionario_pessoa.values():
    print(item)


# O método pop() em Python é usado para remover um item específico de um dicionário e retornar o valor associado a essa chave. Ele funciona de forma semelhante à função pop() para listas, mas em vez de remover um elemento pelo seu índice, remove pelo nome da chave.

resultado = dicionario_2.pop("nome")
print("POP", dicionario_2)

valor = dicionario_2.pop("B", "Chave não encontrada")  # Caso a chave não for encontrada
print(valor)

# Tirar um valor de um dicionario
del dicionario1["a"]
print("DEL", dicionario1)


# Para limpar um dicionario

dicionario_pessoa.clear()
print(dicionario_pessoa)
