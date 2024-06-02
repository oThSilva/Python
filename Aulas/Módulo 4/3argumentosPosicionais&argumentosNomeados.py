def exibir_preco(*, nome_produto, preco):
    print(f"{nome_produto} está no valor de R$ {preco}")


# Argumento posicionais:
# exibir_preco("Iphone", 5000)

# Argumento nomeados. * usar o asterisco para usar só Argumento nomeados na função
exibir_preco(nome_produto="Iphone", preco=5000)

# desafio:


def gerar_objeto_personalizado(cor, *, altura, formato):
    print(f"{cor} {altura} {formato}")


gerar_objeto_personalizado("Vermelho", altura="2.20", formato="quadrado")
