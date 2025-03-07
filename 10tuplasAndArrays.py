# As tuplas em Python são tipos de dados imutáveis que armazenam uma coleção ordenada de elementos.
# Diferentemente das listas, os elementos de uma tupla não podem ser alterados após sua criação.
# Elas são frequentemente usadas para agrupar dados relacionados.

# Tupla: Usa parênteses () ou não usa delimitadores explícitos (packing). Lista: Usa colchetes [].
# Criando uma Tupla
# Com parênteses:
minha_tupla = (1, 2, 3, "a", "b")

# Sem parênteses (packing):
minha_tupla = 1, 2, 3

# Tupla vazia:
minha_tupla = ()

# Tupla de um único elemento: Para evitar confundir uma tupla com um número ou string entre
# parênteses, adicione uma vírgula:
minha_tupla = (5,)

# Acessando Elementos
# Os elementos de uma tupla podem ser acessados usando índices:
minha_tupla = (10, 20, 30, 40)
print(minha_tupla[0])  # 10
print(minha_tupla[-1])  # 40 (último elemento)


# Principais Características
# Imutável: Os elementos não podem ser adicionados, removidos ou alterados.
minha_tupla = (1, 2, 3)
minha_tupla[0] = 10  # Erro: TypeError

# Suporta diferentes tipos de dados:
tupla = (1, "texto", [3, 4, 5], {"chave": "valor"})

# Alinhamento: Uma tupla pode conter outras tuplas:
tupla = (1, (2, 3), (4, 5, 6))
print(tupla[1])  # (2, 3)

# Operações com Tuplas
# Concatenar:
tupla1 = (1, 2)
tupla2 = (3, 4)
resultado = tupla1 + tupla2  # (1, 2, 3, 4)

# Repetir:
tupla = (1, 2)
resultado = tupla * 3  # (1, 2, 1, 2, 1, 2)

# Tamanho da Tupla:
tupla = (1, 2, 3)
print(len(tupla))  # 3

# Verificar Presença de Elemento:
tupla = (1, 2, 3)
print(2 in tupla)  # True
print(4 in tupla)  # False


#Arrays
# Em Python, arrays são coleções ordenadas de elementos, semelhantes às listas, mas otimizadas para armazenar
# grandes volumes de dados homogêneos (do mesmo tipo). Eles são definidos pelo módulo array da biblioteca padrão.

# A principal vantagem de usar arrays é que eles são mais eficientes em termos de memória e desempenho,
# especialmente ao lidar com grandes quantidades de dados numéricos.

# Criando um Array
# Você pode criar um array usando o módulo array:
import array
meu_array = array.array('i', [1, 2, 3, 4])  # 'i' representa inteiros com sinal

# Type Codes
# O type code especifica o tipo de dados que o array armazenará. Cada type code está associado a um tipo
# específico de dado:

type_codes = {
    'b': {'python_type': 'int', 'description': 'Inteiro com sinal', 'size_bytes': 1},
    'B': {'python_type': 'int', 'description': 'Inteiro sem sinal', 'size_bytes': 1},
    'u': {'python_type': 'str', 'description': 'Caracteres Unicode', 'size_bytes': '2 ou 4 (depende da plataforma)'},
    'h': {'python_type': 'int', 'description': 'Inteiro curto com sinal', 'size_bytes': 2},
    'H': {'python_type': 'int', 'description': 'Inteiro curto sem sinal', 'size_bytes': 2},
    'i': {'python_type': 'int', 'description': 'Inteiro padrão com sinal', 'size_bytes': '2 ou 4 (depende da plataforma)'},
    'I': {'python_type': 'int', 'description': 'Inteiro padrão sem sinal', 'size_bytes': '2 ou 4 (depende da plataforma)'},
    'l': {'python_type': 'int', 'description': 'Inteiro longo com sinal', 'size_bytes': 4},
    'L': {'python_type': 'int', 'description': 'Inteiro longo sem sinal', 'size_bytes': 4},
    'q': {'python_type': 'int', 'description': 'Inteiro de 8 bytes com sinal', 'size_bytes': 8},
    'Q': {'python_type': 'int', 'description': 'Inteiro de 8 bytes sem sinal', 'size_bytes': 8},
    'f': {'python_type': 'float', 'description': 'Ponto flutuante de precisão simples', 'size_bytes': 4},
    'd': {'python_type': 'float', 'description': 'Ponto flutuante de precisão dupla', 'size_bytes': 8},
}

# Exemplo de como acessar informações sobre um type code
code = 'f'
info = type_codes.get(code, 'Type code não encontrado')
print(f"Type code '{code}': {info}")


# Operações com Arrays
# Criar um Array:

arr = array.array('f', [1.0, 2.5, 3.2])  # Array de floats

# Acessar Elementos:
print(arr[1])  # 2.5

# Adicionar Elementos:
arr.append(4.5)  # Adiciona 4.5 ao final

# Remover Elementos:
arr.remove(2.5)  # Remove o elemento 2.5

# Obter o Type Code:
print(arr.typecode)  # 'f' (para um array de floats)

# Conversão para Lista:
lista = arr.tolist()  # Converte o array para uma lista
