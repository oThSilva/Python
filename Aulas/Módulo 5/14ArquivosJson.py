import json
from pathlib import Path

carros = [
    {"Marca": "Nissan", "Preco": 45000, "Cor": "Azul"},
    {"Marca": "Ford", "Preco": 75000, "Cor": "Verde"},
    {"Marca": "BMW", "Preco": 115000, "Cor": "Amarelo"},
]
carros_json = json.dumps(
    carros
)  # Convertendo um objeto python para uma representação JSON(string)
Path("carros.json").write_text(carros_json)
# Cria um objeto "path" representando o caminho do arquivo "carros.json". Escreve o conteudo da string "carros_json"(que contem o JSON) para o arquivo "carros.json"

arquivo_carros_Json = Path("carros.json").read_text()
# O código lê o conteúdo do arquivo "carros.json" como uma string de texto e armazena a mesma na variável "arquivo_carros_Json"
print(arquivo_carros_Json)

arquivo_json = json.loads(arquivo_carros_Json)
# loads é uma função pra carregar uma string json, convertendo-a em um objeto python, "arquivo_json" é a variável que contem uma estrutura de dados python


print(arquivo_json[0]["Marca"] + " " + str(arquivo_json[0]["Preco"]))
print(arquivo_json[1]["Marca"] + " " + str(arquivo_json[1]["Preco"]))
