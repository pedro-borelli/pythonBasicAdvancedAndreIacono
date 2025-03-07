# List comprehension é uma maneira concisa e elegante de criar listas em Python.
# É frequentemente usada como alternativa a loops for quando você deseja criar ou transformar listas.
#
# Sintaxe Básica
# [nova_expressao for item in iteravel]
#
# nova_expressao: O valor ou transformação aplicada a cada elemento.
# item: Cada elemento do iterável (ex.: lista, tupla, conjunto).
# iteravel: A coleção que será iterada.


# Exemplo Básico
# Criando uma lista com os quadrados dos números de 1 a 5:
quadrados = [x**2 for x in range(1, 6)]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]

# Com Condição
# Adicionando uma condição para incluir apenas números pares:
pares = [x for x in range(1, 11) if x % 2 == 0]
print(pares)  # Saída: [2, 4, 6, 8, 10]


# Com Transformação e Condição
# Multiplicando números ímpares por 2:
resultado = [x * 2 for x in range(1, 11) if x % 2 != 0]
print(resultado)  # Saída: [2, 6, 10, 14, 18]

# Comparação com Loop For
# Criar uma lista de números pares de 1 a 10.
#
# Com Loop For:
pares = []
for x in range(1, 11):
    if x % 2 == 0:
        pares.append(x)

print(pares)  # Saída: [2, 4, 6, 8, 10]


# Com List Comprehension:
pares = [x for x in range(1, 11) if x % 2 == 0]
print(pares)  # Saída: [2, 4, 6, 8, 10]

# A list comprehension é mais compacta e legível.


