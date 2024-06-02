# Polimorfismo é um conceito da programação orientada a objetos que se refere à capacidade de objetos de diferentes classes responderem ao mesmo método de forma diferente. Isso significa que métodos com o mesmo nome podem ser implementados de maneiras diferentes em classes diferentes.
# Métodos com o mesmo nome: Polimorfismo ocorre quando várias classes têm um método com o mesmo nome.
# Comportamentos diferentes: Cada classe pode implementar o método de maneira diferente, realizando operações específicas para aquela classe.
# Chamada de métodos: Mesmo chamando o mesmo método em objetos de classes diferentes, o comportamento do método pode variar dependendo da classe do objeto.
# Por exemplo, considere as classes Cao e Gato, ambas com o método emitir_som(), mas com comportamentos diferentes para esse método:


class Cao:
    def emitir_som(self):
        return "Au Au!"


class Gato:
    def emitir_som(self):
        return "Miau!"


# Exemplo de polimorfismo
def fazer_som(animal):
    print(animal.emitir_som())


# Chamando a função fazer_som com diferentes tipos de animais
cao = Cao()
gato = Gato()

fazer_som(cao)  # Saída: Au Au!
fazer_som(gato)  # Saída: Miau!


# Polimorfismo com Herança


class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo
