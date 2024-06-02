# # kwargs(keyword arguments) O **kwargs permite que você passe um número variável de argumentos nomeados para a função. O duplo asterisco ** antes de kwargs é uma convenção, mas o nome pode ser qualquer um. Dentro da função, kwargs é tratado como um dicionário contendo todos os argumentos nomeados fornecidos, onde as chaves são os nomes dos parâmetros e os valores são os valores associados.
def detalhes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")


detalhes(
    nome="João", idade=30, cidade="São Paulo"
)  # Chamada da função com argumentos nomeados

# def contatenar(**palavras):
#     frase = ""
#     for palavra in palavras.values():
#         frase += palavra + " "
#     print(frase)


# contatenar(a="Sou", b="Um", c="'Pythonista", d="Autodidata")


def funcao(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)


funcao("Th", 5, 6, 7, 8, 9, a=1, b=2, c=3)


def exibir_carros(*kwarks):
    lista_de_carro = " "
    for carro in kwarks:
        lista_de_carro += carro + " "
    print(lista_de_carro)


exibir_carros("Gol", "Vectra", "Celta")
