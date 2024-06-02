idade = input("Sua idade: ")
print(int(idade) > 17)

ano_publicacao = 2020
print("Esse livro sera publicado em " + str(ano_publicacao))

altura = input("Altura da parede: ")
print(float(altura) > 2.50)

# conversão entre coleções
saudacao = "Olá!"
print(list(saudacao))
print(set(saudacao))
print(tuple(saudacao))

numeros = [10, 20, 30, 40, 50, 50]
print(set(numeros))
print(tuple(numeros))
print(type(numeros))
