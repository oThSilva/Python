# #Separar(Spilt)
# frase = 'Olá, bem-vindo a este treinamento'
# print(frase.split())
# print(frase.split(','))
# print(frase.split('-'))
# nomes = 'Thiago, Ryan, Pedroso, Amandino'
# print(nomes.split())
# print(nomes.split(','))
# hashtags = 'music #guitar #gamer #coder #python'
# print(hashtags.split())
# print(hashtags.split('#'))
# print(hashtags.split('#', 3)) #1º parametro: qual separador ele vai usar 2º: quantas ocorrencias

# #Juntar(Join)
# hashtags_separadas_por_espaco = hashtags.split(' ')
# print(hashtags_separadas_por_espaco)
# print(','.join(hashtags_separadas_por_espaco))
# print('.'.join(hashtags_separadas_por_espaco))
# print(' '.join(hashtags_separadas_por_espaco))

#Desafio

frase1 = "Desafio manipulação de strings"
palavras1 = frase1.split()
print(palavras1)
print(','.join(palavras1))

frase2 = "jhonatan,rafael,carol,camilla"
palavras2 = frase2.split(',')
print(palavras2)
print(' & '.join(palavras2))