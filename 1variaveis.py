# Em Python, as variáveis são usadas para armazenar valores e estão associadas a tipos de dados.
# Python é uma linguagem de tipagem dinâmica, o que significa que não é necessário declarar o
# tipo de uma variável explicitamente — o Python infere o tipo com base no valor atribuído.

# Abaixo estão os principais tipos de variáveis (tipos de dados) em Python, com exemplos:

# Texto (String): Armazena sequências de caracteres (texto).
# Strings são declaradas com aspas simples (') ou duplas (").
nome = "João"
saudacao = 'Olá, tudo bem?'
print(str(nome))

# Numéricos: usados para armazenar números. Podem ser de três tipos principais:

# int: Números inteiros.
# float: Números de ponto flutuante (decimais).
# complex: Números complexos (com parte real e imaginária).

# Inteiro
idade = 25
print(int(idade))

# Ponto flutuante
altura = 1.75
print(float(altura))

# Número complexo
numero_complexo = 2 + 3j
print(complex(numero_complexo))

# Booleano (bool) Representa valores lógicos: True (verdadeiro) ou False (falso).
is_estudante = True
is_maior_de_idade = False
print(bool(is_estudante))
print(bool(is_maior_de_idade))

# Sequências Agrupam múltiplos valores em uma única variável:

# list: Lista mutável (pode ser alterada).
# tuple: Tupla imutável (não pode ser alterada).
# range: Representa uma sequência de números.

# Lista
frutas = ["maçã", "banana", "uva"]
print(list(frutas))

# Tupla
cores = ("vermelho", "azul", "verde")
print(tuple(cores))

# Range
# Gerar lista com (fim)
print(list(range(5)))

# Gerar com (inicio, fim)
print(list(range(5, 10)))

# Gerar com (inicio, fim, passo)
print(list(range(0, 10, 2))) # a lista vai do 0 ao 10 pulando de 2 em 2

# Mapeamento dict: Armazena pares de chave e valor.
pessoa = {"nome": "Ana", "idade": 30, "cidade": "São Paulo"}
print(dict(pessoa))


# Use type(): Quando você precisa saber exatamente o tipo de um objeto, sem considerar herança.
# Use isinstance(): Quando deseja verificar se um objeto pertence a uma classe ou suas subclasses,
# ou validar múltiplos tipos.

class Animal:
    pass

class Cachorro(Animal):
    pass

rex = Cachorro()

# Usando type()
print(type(rex) == Animal)  # False

# Usando isinstance()
print(isinstance(rex, Animal))  # True


# Características
# type(): Retorna o tipo exato do objeto. Não reconhece subclasses. Não aceita verificação múltipla.
# isinstance(): Retorna True ou False. Reconhece subclasses. Permite verificar vários tipos.

# A variável None em Python representa a ausência de valor ou a falta de um valor válido.
# É um objeto especial que é usado como um marcador para situações onde uma variável ainda não foi inicializada,
# não possui valor ou quando uma função não retorna nenhum resultado explicitamente.

# Inicializar Variáveis
# Usado para indicar que uma variável ainda não possui valor.

resultado = None
# if condição:
#     resultado = 42
print(resultado)

# Funções sem return explícito
# Uma função que não retorna nada retorna implicitamente None.

def exemplo():
    pass

retorno = exemplo()
print(retorno)  # Saída: None

# Valor padrão em argumentos
# Usado para indicar que um argumento é opcional.

def saudacao(nome=None):
    if nome:
        print(f"Olá, {nome}!")
    else:
        print("Olá, visitante!")

saudacao("João")  # Saída: Olá, João!
saudacao()        # Saída: Olá, visitante!

# Resetar valores
# Indica que um valor foi apagado ou não está mais disponível.

valor = 100
print(valor)  # Saída: 100
valor = None
print(valor)  # Saída: None







