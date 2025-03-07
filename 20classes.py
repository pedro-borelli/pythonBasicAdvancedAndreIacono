# Em Python, classes são usadas para criar objetos e modelar tipos de dados personalizados, enquanto
# construtores são métodos especiais que inicializam esses objetos. Vamos detalhar:

# Definindo Classes
# Para definir uma classe em Python, usa-se a palavra-chave class.
# Uma classe pode conter atributos (dados) e métodos (funções associadas aos objetos dessa classe).
class MinhaClasse:
    # Método da classe
    def metodo(self):
        print("Este é um método da classe.")

# Construtores
# O construtor em Python é o método especial chamado __init__.
# Ele é chamado automaticamente quando uma nova instância da classe é criada.

# Exemplo básico:
class Pessoa:
    def __init__(self, nome, idade):
        # Inicializando os atributos do objeto
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando uma instância da classe
pessoa = Pessoa("João", 25)
pessoa.apresentar()

# Saída:
# Olá, meu nome é João e eu tenho 25 anos.

# Detalhes sobre o Construtor
# __init__ não é obrigatório: Se não for definido, a classe usará um construtor padrão.
# Parâmetros personalizados: Você pode adicionar quantos parâmetros forem necessários no __init__,
# além do padrão self.

# Atributos da classe: O uso de self.atributo cria atributos específicos para a instância.
# Atributos e Métodos da Classe vs. Instância
# Atributos da Instância: Específicos para cada objeto.


# Atributos da Classe: Compartilhados entre todas as instâncias. Declarados fora do __init__.
class Exemplo:
    atributo_classe = "Compartilhado"

    def __init__(self, valor):
        self.atributo_instancia = valor

obj1 = Exemplo("Objeto 1")
obj2 = Exemplo("Objeto 2")

print(obj1.atributo_classe)  # Compartilhado
print(obj1.atributo_instancia)  # Objeto 1


# Herança e Construtores
# Uma classe pode herdar outra classe, e o construtor pode ser sobreposto.
class Animal:
    def __init__(self, especie):
        self.especie = especie

class Cachorro(Animal):
    def __init__(self, especie, nome):
        super().__init__(especie)  # Chamando o construtor da classe base
        self.nome = nome

dog = Cachorro("Canino", "Rex")
print(f"Espécie: {dog.especie}, Nome: {dog.nome}")

# Saída:
# Espécie: Canino, Nome: Rex