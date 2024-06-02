# pip
# pip é o instalador de pacotes oficial para Python. Ele permite que você instale, atualize e remova pacotes Python que estão disponíveis no Python Package Index (PyPI), um repositório de software para a linguagem Python.

# Principais Comandos do pip
# Instalar um pacote:
# pip install nome_do_pacote

# Atualizar um pacote:
# pip install --upgrade nome_do_pacote

# Desinstalar um pacote:
# pip uninstall nome_do_pacote

# Listar pacotes instalados:
# pip list

# Ver informações sobre um pacote:
# pip show nome_do_pacote

# Exemplo de Uso
# Para instalar o pacote requests, você pode usar o seguinte comando:
# pip install requests

# Depois de instalado, você pode usá-lo no seu código Python:

# import requests

# response = requests.get('https://api.github.com')
# print(response.status_code)

# Resumo
# Pacotes: São uma maneira de organizar e estruturar seu código Python em módulos e submódulos.
# pip: É uma ferramenta de linha de comando que permite instalar, atualizar e gerenciar pacotes Python de forma simples e eficiente.
# Juntos, pacotes e pip facilitam a modularização do código e o gerenciamento de dependências em projetos Python.

# Pacotes são uma maneira de organizar módulos Python em diretórios hierárquicos. Cada pacote é essencialmente um diretório que contém um arquivo especial chamado __init__.py, que pode estar vazio ou conter código de inicialização do pacote. Pacotes permitem que você estruture seu código de forma organizada, facilitando a manutenção e a reutilização de componentes.

# Módulo: Um arquivo Python contendo definições e implementações de funções, classes e variáveis.
# Pacote: Um diretório contendo um ou mais módulos e um arquivo __init__.py.
# Exemplo de Estrutura de Pacote:
# meu_pacote/
# __init__.py
# modulo1.py
# modulo2.py
# subpacote/
#     __init__.py
#     modulo3.py
# Para usar um módulo de um pacote, você pode usar a sintaxe de importação:
# from meu_pacote import modulo1
# import meu_pacote.subpacote.modulo3
