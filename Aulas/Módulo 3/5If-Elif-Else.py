numero_atrasos = 3
if numero_atrasos > 2:
    print('Não pode entrar')
elif (numero_atrasos == 2):
    print('Essa é a última vez que podera chegar atrasado')
else:
    print('Pode entrar')

#Chaining = encadeamento de métodos. Encadeamento de métodos de string    
frase = "olá, mundo!"


resultado = frase.upper().replace('OLÁ', 'Olá').capitalize()

print(resultado)

#desafio
comprimento_cabelo = int(input('Comprimento do cabelo:'))
valor = float(0)
if comprimento_cabelo <= 20:
    valor = 50
    print(f'cabelo de {comprimento_cabelo}cm você paga o valor de R$ {valor}')
elif comprimento_cabelo <= 30:
    valor = 70
    print(f'cabelo de {comprimento_cabelo}cm você paga o valor de R$ {valor}')
elif comprimento_cabelo <= 50:
    valor = 100
    print(f'cabelo de {comprimento_cabelo}cm você paga o valor de R$ {valor}')
else:
    print('Favor consultar na recepção')

