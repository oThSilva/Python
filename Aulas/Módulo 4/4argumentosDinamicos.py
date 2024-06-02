# *args(argumentos posicionais) O *args permite que você passe um número variável de argumentos posicionais para a função. O asterisco * antes de args é uma convenção, mas o nome pode ser qualquer um. Dentro da função, args é tratado como uma tupla contendo todos os argumentos posicionais fornecidos.
def somar(*valores, b):
    print(valores)
    for valor in valores:
        b += valor
        print(b)


somar(10, 20, 5, b=5)
