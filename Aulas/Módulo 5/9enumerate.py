# for indice, numero in enumerate(range(1, 11), 1):
#     print(indice, numero)

frutas = ["Maçã", "laranja", "Morango", "Limão"]

for indice, fruta in enumerate(frutas, 0):
    if indice == 3:
        print(f"{indice} {fruta} EM PROMOÇÃO")
    else:
        print(indice, fruta)
