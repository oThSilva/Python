from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Usar a função With
# with expressao as variavel:
# Bloco de código indentado
# A instrução with em Python é usada para criar um contexto de execução com um objeto que suporta o protocolo de gerenciamento de contexto. Isso é útil para garantir que recursos sejam liberados automaticamente após a conclusão de uma operação, mesmo em caso de exceção.

# Verificar se o arquivo foi aberto com sucesso usando Try e except


try:
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")


# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")

# Usar a codificação correta no argumento encoding="utf-8"

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
except UnicodeDecodeError as exc:
    print(exc)
