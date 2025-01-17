# Desafio
# Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto.

# Formato esperado:
# O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9. Lembre-se de respeitar os espaços entre os números quando preciso.

# Entrada
# Uma string representando o número de telefone.

# Saída
# Uma mensagem indicando se o número de telefone é válido ou inválido.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	            Saída
# (88) 98888-8888       Número de telefone válido.

import re


# def validate_numero_telefone(phone_number):
#     pattern = r"^\(\d{2}\) \d{5}-\d{4}$"
#     if re.match(pattern, phone_number):
#         return True
#     else:
#         return False


# validar_telefone = input("Digite o numero de telefone")
# print(validate_numero_telefone(validar_telefone))


def validate_numero_telefone(phone_number):
    pattern = r"^\(\d{2}\) \d{5}-\d{4}$"
    if re.match(pattern, phone_number):
        print("Número de telefone válido.")
    else:
        print("Número de telefone inválido.")


phone_number = "(14) 99128-4589"
validate_numero_telefone(phone_number)
