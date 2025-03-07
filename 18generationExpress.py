# Generation expression (expressão geradora) em Python é semelhante a uma list comprehension, mas,
# em vez de criar uma lista completa na memória, ela gera os elementos um por um, sob demanda, usando menos memória.

# Sintaxe
# A sintaxe de uma expressão geradora é semelhante à de uma list comprehension, mas usa parênteses ()
# em vez de colchetes []:

# ( expressão for item in iterável if condição )

# Diferenças Principais com List Comprehensions

# Economia de Memória:
# List comprehensions criam toda a lista na memória.
# Expressões geradoras geram os valores um por um, sob demanda.

# Tipo Retornado:
# List comprehension retorna uma lista.
# Generator expression retorna um objeto gerador.

# Exemplo Simples
# Criando uma expressão geradora para números ao quadrado:

# Expressão geradora
quadrados = (x**2 for x in range(5))

print(quadrados)  # Saída: <generator object ...>
print(list(quadrados))  # Saída: [0, 1, 4, 9