import random

print(random.random()) #entre 0.0 e 1.0
print(random.uniform(4, 10)) #entre 4 e 10 (tipo float)
print(random.randint(4 ,10)) #entre 4 e 10 (tipo inteiro)

cores = ['verde','vermelho','azul'] #escolher opção aleatória
print(random.choice(cores))
print(random.choices(cores, k=2)) #k = para escolher a quantidade de escolhas

cartas_de_um_baralho = ['carta1','carta2','carta3','carta4'] #embaralhar lista
print(random.shuffle(cartas_de_um_baralho))
print(cartas_de_um_baralho)

#desafio1
moeda = ['Cara','Coroa']
print(f'Lado da moeda: {random.choice(moeda)} .Das opções {moeda}')

#desafio2
nomes = ['th','nega','annabeth','gaby','hunter']
print(f'Nome escolhido: {random.choice(nomes)} .Das opções {nomes}')

#desafio3
print(f'Numero aleatório de 10 a 100: {random.randint(10,100)}')



