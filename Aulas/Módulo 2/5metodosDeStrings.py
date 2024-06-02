nome_curso = " Edição de música "
print(
    nome_curso.title()
)  # Retorna uma versão da string com o primeiro caracter maiúsculo e todos os caracteres restantes têm letras minúsculas.
print(nome_curso.upper())  # todas letras são maiuscula
print(nome_curso.lower())  # todas letras são minuscula
print(nome_curso.strip())  # tira toda o espaço em branco
print(nome_curso.lstrip())  # tira toda o espaço em branco da esquerda
print(nome_curso.rstrip())  # tira toda o espaço em branco da direita
print(nome_curso.find("ção"))  # encontra o index
print(nome_curso.replace("música", "Vídeo"))  # substitui o caracter

# DESAFIO
# Através da criação de string dinâmicos e os métodos de um string que acabou de aprender, use como base as variáveis a seguir para criar as seguintes frases
a = "é"
b = "MELHOR"
c = "QUE"
d = "feito"
e = "perfeito"

print(f"{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}")
