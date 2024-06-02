# Crie um programa que solicita ao usuário que insira três notas (valores de 0 a 10) e, em seguida, calcule e exiba a média dessas notas.

# Além disso, informe ao usuário se ele foi aprovado ou reprovado com base na média das notas, considerando a média mínima de aprovação como 6.


notas = []

while True:
    nota = float(input("Digite a nota: "))
    if nota < 0 or nota > 10:
        print("Digite somente notas de 0 a 10")
    else:
        notas.append(nota)
        if len(notas) == 3:
            break

media = (sum(notas)) / 3

if media >= 6:
    print(f"Aluno aprovado com media {media}")
else:
    print(f"Aluno reprovado com media {media}")
