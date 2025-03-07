# A função map() é uma função embutida no Python que aplica uma função a cada item de um iterável
# (como listas, tuplas ou conjuntos) e retorna um iterador contendo os resultados.
# Ela é muito útil quando você deseja transformar uma sequência de dados sem usar um loop explícito.

# Sintaxe
# map(funcao, iteravel)

# funcao: A função que será aplicada a cada item do iterável.
# iteravel: O iterável cujos itens serão transformados pela função.

# Exemplo Simples
# Dobrando números de uma lista:

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Função para dobrar um número
def dobrar(numero):
    return numero * 2

# Usando map
resultado = map(dobrar, numeros)

# Convertendo o resultado em uma lista
print(list(resultado))  # Saída: [2, 4, 6, 8, 10]

# Usando map com Funções Lambda
# Você pode usar uma função lambda para evitar criar uma função separada:
numeros = [1, 2, 3, 4, 5]

# Usando lambda dentro do map
resultado = map(lambda x: x * 2, numeros)

print(list(resultado))  # Saída: [2, 4, 6, 8, 10]


# A função filter() é uma função embutida no Python que serve para filtrar elementos de um iterável
# (como listas, tuplas ou conjuntos) com base em uma condição definida por uma função. Apenas os itens para
# os quais a função retorna True são mantidos no resultado.

# Sintaxe
# filter(funcao, iteravel)

# funcao: Uma função que retorna True ou False para cada item do iterável.
# iteravel: O iterável que será filtrado.

# A função retorna um iterador, por isso geralmente é convertido para um tipo como lista ou tupla.

# Exemplo Simples
# Filtrando números pares de uma lista:

# Lista de números
numeros = [1, 2, 3, 4, 5, 6]

# Função que verifica se um número é par
def eh_par(numero):
    return numero % 2 == 0

# Usando filter
resultado = filter(eh_par, numeros)

# Convertendo para lista e exibindo
print(list(resultado))  # Saída: [2, 4, 6]


# Usando filter com Funções Lambda
# Uma função lambda torna o código mais compacto:
numeros = [1, 2, 3, 4, 5, 6]

# Usando filter com lambda
resultado = filter(lambda x: x % 2 == 0, numeros)

print(list(resultado))  # Saída: [2, 4, 6]