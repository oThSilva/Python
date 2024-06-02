paises = ['Brasil','Alemenha','Russia']
estacoes_do_ano = ['Primaveira','Verão','Outono','Inverno']
for pais in paises:
    for estacao in estacoes_do_ano:
        print(f'{pais} {estacao}')

for x in range(1, 11):
    for y in range(1, 6):
        print(f'Valor externo {x} e interno de {y}')
    
#desafio
celulares = ['Asus','Samsung','Sony','Iphone']
versoes = ['Plus','Premuim Plus','Peemium Deluxe','Plus Premium Ultra']
for celular in celulares:
    for versao in versoes:
        print(f'{celular} {versao}')
