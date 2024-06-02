# Conclua a solução para que ela divida a cadeia de caracteres em pares de dois caracteres. Se a cadeia de caracteres contiver um número ímpar de caracteres, ela deverá substituir o segundo caractere ausente do par final por um sublinhado ('_').

# Exemplos:

# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']


def solution(s):
    pares = []
    if len(s) % 2 != 0:
        s += "_"

    for i in range(0, len(s), 2):
        par = s[i : i + 2]
        pares.append(par)

    return pares


texto = "abcdefg"
resposta = solution(texto)
print(resposta)
