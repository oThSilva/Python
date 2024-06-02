# A função property() em Python é usada para criar propriedades em uma classe, o que permite controlar o acesso, a atribuição e a deleção de atributos de objetos dessa classe. Em resumo, ela ajuda a definir métodos para acessar, modificar e deletar atributos de uma forma mais controlada. Ela é comumente usada quando você quer adicionar métodos getter, setter e deleter para um atributo de uma classe, para assim controlar melhor como esse atributo é acessado, modificado ou deletado.

# Sintaxe:
# property(fget=None, fset=None, fdel=None, doc=None)
# Argumentos:
# fget: Método que será chamado quando o atributo é acessado (getter).
# fset: Método que será chamado quando o atributo é modificado (setter).
# fdel: Método que será chamado quando o atributo é deletado (deleter).
# doc: String opcional que especifica a documentação da propriedade.
# Retorno:
# Um objeto property.


class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # Atributo privado

    # Getter
    def get_nome(self):
        return self._nome

    # Setter
    def set_nome(self, novo_nome):
        self._nome = novo_nome

    # Deleter
    def del_nome(self):
        del self._nome

    # Criando uma propriedade para o atributo nome
    nome = property(get_nome, set_nome, del_nome, "Nome da pessoa")


# Usando a classe Pessoa
p = Pessoa("João")
print(p.nome)  # Acessando o atributo nome usando a propriedade
p.nome = "Maria"  # Modificando o atributo nome usando a propriedade
print(p.nome)
del p.nome  # Deletando o atributo nome usando a propriedade

# ou:


class Pessoa2:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa2
("Thiago", 2000)
print(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade} anos")
