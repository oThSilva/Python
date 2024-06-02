for numero in range(10):
    if numero == 5:
        continue 
    print(numero)

print('Fim')
#A instrução continue é usada para pular o restante do código dentro de um loop e continuar para a próxima iteração.

for numero in range(10):
    if numero == 5:
        break
    print(numero)

print('Fim')

#A instrução break é usada para interromper a execução de um loop antes que ele seja concluído

#desafio 1
estilos = ['Hip Hop','Rock','Rap','Pop']
for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(estilo)
#desafo 2
estilos = ['Hip Hop','Rock','Rap','Pop']
for estilo in estilos:
    if estilo == 'Rock':
        break
    print(estilo)
