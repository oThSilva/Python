# Desafio
# Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.

# Entrada
# O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.

# Saída
# Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	    Saída
#               Lista de Equipamentos:
# Antena        - Antena
# Roteador      - Roteador
# Switch        - Switch


def obter_itens():
    itens = []
    for _ in range(3):
        item = input("Digite um item (ou deixe em branco para terminar): ").strip()
        if not item:
            break
        itens.append(item)
    return itens


def exibir_lista(itens):
    print("Lista de Equipamentos:")
    for item in itens:
        print(f"- {item}")


def main():
    itens = obter_itens()
    exibir_lista(itens)


main()
