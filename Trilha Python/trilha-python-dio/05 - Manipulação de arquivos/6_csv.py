# Praticas Recomendadas:
# Usar o csv.reader e csv.writer para manipular arquivos CSV.
# Fazer tratamento correto das exceções.
# Ao gravar arquivos CSV definir o argumento newline = "" No método "open"

import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1

# Escrevendo um arquivo CSV
# try:
#     with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(["id", "nome"])
#         escritor.writerow(["1", "Maria"])
#         escritor.writerow(["2", "João"])
# except IOError as exc:
#     print(f"Erro ao criar o arquivo. {exc}")

# Para ler arquivos CSV

try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f"ID: {row[COLUNA_ID]}")
            print(f"Nome: {row[COLUNA_NOME]}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")

# Para ler arquivos CSV
try:
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
