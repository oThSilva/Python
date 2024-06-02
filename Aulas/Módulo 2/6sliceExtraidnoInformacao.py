teclado = "Teclado"
print(teclado[1])  # =e
print(teclado[-1])  # para acessar o ultimo indice
print(teclado.index("l"))  # para acessar um index dentro da string
print(teclado[teclado.index("l")])  # para buscar o carater
print(teclado[0:5])  # imprimir um intervalo especifico de uma string
print(teclado[0:])  # para imprimir toda a string
print(teclado[-5:])  # de tras pra frente
print(teclado[5:])  # exibir as informações a partir de um indice
print(teclado[:-5])  # exibibir de tras pra frente
print(teclado[::-1])  # inverte a string
# print(teclado.rindex('C')) #para acessar de ultima ocorrencia um caracter de uma string

# Desafio1
biblioteca = "Biblioteca"
print(biblioteca.index("o"))
# Desafio2
frase = "Desenvolvimento De Aplicações"
print(frase[16:])
# Solução 2
indice_d = frase.rindex("D")
indice_s = frase.rindex("s")
print(frase[indice_d : indice_s + 1])
