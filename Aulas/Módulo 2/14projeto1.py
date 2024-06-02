from datetime import datetime
import random

nome_usuario = input('Digite seu nome: ')
idade_usuario = input('Digite sua idade: ')
data_aniversario = datetime.strptime(input('Qual a data do seu aniversário? '), '%d/%m/%Y')
data_cadastro = datetime.now()
cartoes = ['R$ 50,00','R$ 250,00','R$120,00']
cartao_sortido = random.choice(cartoes)

print(f'Olá {nome_usuario}, seu registro foi concluído com sucesso no dia {data_cadastro}.\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao_sortido}')