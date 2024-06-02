# Para simplificar, você terá que colocar cada palavra com a primeira letra em maiúscula.


def to_jaden_case(string):
    palavras = string.split()

    for palavra in range(len(palavras)):
        palavras[palavra] = palavras[palavra][0].upper() + palavras[palavra][1:]

    return " ".join(palavras)


frase = "texto exemplo que eu escolhi para exemplificar"
para_maiusculo = to_jaden_case(frase)
print(frase)
print(para_maiusculo)
