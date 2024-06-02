# No domínio da programação, as expressões regulares (RegEx no Python) aplicam conceitos da chamada teoria da computação de uma forma mais prática e usual. Permite compreender formatos de strings e processá-las com determinadas funções

# Sintaxe e metacaracteres em RegEx: O Regex no Python segue uma lista de elementos e de significados para possibilitar que as operações sejam executadas.

# [] - conjunto de caracteres
# \ - sequencia especial de carateres
# ^ - buscar elementos no inicio da string
# $ - buscar elementos no final da string
# * - buscar zero ou mais repetições de um substring
# + - uma ou mais aparições de uma substring
# ? - zero ou uma aparição
# | busca um caractere ou outro

# Biblioteca re para operações com RegEx
# 1. re.match: A sintaxe é re.match(padrão, string, flags=0) e tenta encontrar um padrão dentro de uma string. Por exemplo, seguindo o exemplo que já mencionamos, você pode usar para tentar achar o padrão de um CPF. Caso a função não encontre o que procura, vai retornar None.
# 2. re.findall: Para retornar uma lista de elementos com aquele padrão, use o findall. Ele é muito útil quando você necessita de todas as ocorrências de uma substring, em um dado padrão, para então manipular isso de alguma forma. Um exemplo de uso é captar todos os advérbios de uma frase, por exemplo.
# 3. re.sub: Serve para buscar um padrão e substituí-lo por outro. Então, retorna uma nova string, a que tomou o lugar da anterior. Em caso de não encontrar o padrão, retorna a string normal.
# 4. re.finditer: Essa função faz uma iteração de strings em busca de um dado padrão. A sintaxe é finditem(padrão, string, flags). Ou seja, faz um loop entre as correspondentes para localizá-las e retorna também o índice dessas strings. Aliás, essa é a diferença para o findall: o retorno do índice.
# 5. re.search: Permite a busca por um padrão e retorna informações completas, como a posição inicial e a final daquele padrão dentro de uma string, além, é claro, da própria string. Essa função retorna somente a primeira ocorrência de uma dada string. Para encontrar todas as aparições, você deve recorrer ao findall, como já falamos.

import re


def validar_telefone(telefone):
    padrao = r"^\(\d{2}\) \d{5}-\d{4}$"

    if re.match(padrao, telefone):
        return True
    else:
        return False


numeros_telefone = [
    "(11) 12345-6789",
    "(88) 98888-8888",
    "1234567890",
    "(88) 12345-6789",
    "(99) 9999-9999",
]

for telefone in numeros_telefone:
    if validar_telefone(telefone):
        print(f"{telefone} é um numero de telefone válido\n")
    else:
        print(f"{telefone} é um numero de telefone inválido\n")
