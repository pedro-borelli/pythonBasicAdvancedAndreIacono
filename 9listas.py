# sum	Soma os valores de um iterável	sum([1, 2, 3]) → 6
# Soma de uma lista
numeros = [1, 2, 3, 4, 5]
print(sum(numeros))  # Saída: 15

# Soma com valor inicial
print(sum(numeros, 10))  # Saída: 25 (15 + 10)

# Soma de tupla
print(sum((10, 20, 30)))  # Saída: 60

# podemos usar min e max para saber o valor minímo ou máximo de uma lista
# podemos perguntar utilizando IN para saber se o valor existe dentro da lista

# sorted	Retorna uma lista ordenada	sorted([3, 1, 2]) → [1, 2, 3]
# Ordenar uma lista de números
numeros = [5, 3, 8, 1]
print(sorted(numeros))  # Saída: [1, 3, 5, 8]

# Ordenar em ordem decrescente
print(sorted(numeros, reverse=True))  # Saída: [8, 5, 3, 1]

# Ordenar strings por comprimento
palavras = ["banana", "kiwi", "maçã", "laranja"]
print(sorted(palavras, key=len))  # Saída: ['kiwi', 'maçã', 'banana', 'laranja']

# len	Retorna o número de elementos	len([1, 2, 3]) → 3
# Comprimento de uma lista
numeros = [1, 2, 3, 4]
print(len(numeros))  # Saída: 4

# Comprimento de uma string
texto = "Python"
print(len(texto))  # Saída: 6

# Comprimento de um dicionário
dicionario = {"a": 1, "b": 2, "c": 3}
print(len(dicionario))  # Saída: 3

# reversed	Retorna um iterador para a sequência invertida	list(reversed([1, 2, 3])) → [3, 2, 1]
# Inverter uma lista
numeros = [1, 2, 3, 4]
print(list(reversed(numeros)))  # Saída: [4, 3, 2, 1]

# Inverter uma string
texto = "Python"
print("".join(reversed(texto)))  # Saída: "nohtyP"

# Inverter uma tupla
tupla = (10, 20, 30)
print(tuple(reversed(tupla)))  # Saída: (30, 20, 10)

# As funções append e pop são métodos usados com listas em Python para adicionar e remover elementos
# de forma prática e eficiente.
# Simulando uma pilha (stack) com lista
pilha = []

# Adicionar elementos à pilha
pilha.append(1)
pilha.append(2)
pilha.append(3)
print("Pilha após append:", pilha)  # Saída: [1, 2, 3]

# Remover elementos da pilha (último a entrar é o primeiro a sair)
print("Elemento removido:", pilha.pop())  # Saída: 3
print("Pilha após pop:", pilha)  # Saída: [1, 2]

# O método insert em Python é usado para adicionar um elemento em uma posição específica de uma lista.
numeros = [1, 2, 3]
numeros.insert(1, 10)  # Insere o número 10 na posição 1
print(numeros)  # Saída: [1, 10, 2, 3]
