nomes = ["Larissa", "Rafael", "Marcos", "Jonh"]


def pessoa_aprovada(pessoa):
    if pessoa == "Marcos":
        return True
    else:
        return False


print(list(filter(pessoa_aprovada, nomes)))
print(list(map(pessoa_aprovada, nomes)))

pinturas = [
    ["pintura classica, ", "Azul", 1857],
    ["pintura medieval, ", "Vermelha", 1867],
    ["pintura Moderna, ", "Verde", 1897],
]


def pintura_antiga(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False


print(list(filter(pintura_antiga, pinturas)))

vagas = [
    ["Vaga 1", 1200],
    ["Vaga 2", 2550],
    ["Vaga 3", 5000],
]


def salario_maior_2500(salario):
    if salario[1] > 2500:
        return True
    else:
        return False


print(list(filter(salario_maior_2500, vagas)))
