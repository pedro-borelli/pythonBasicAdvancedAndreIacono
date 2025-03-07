# crie um script que peça para o usuario digitar o nome de 5 bebidas favoritas dele,
# armazenando esses valores em uma lista. Na sequencia exiba na tela os elementos da lista
# em ordem alfabetica, por linha, usando um laço de repetição for

# Criando uma lista para armazenar as bebidas favoritas
bebidas = []

# Solicitando ao usuário os nomes das 5 bebidas
print("Digite o nome das suas 5 bebidas favoritas:")
for i in range(5):
    bebida = input(f"Bebida {i + 1}: ")
    bebidas.append(bebida)

# Ordenando a lista em ordem alfabética
bebidas.sort()

# Exibindo os elementos da lista em ordem alfabética
print("\nSuas bebidas favoritas em ordem alfabética são:")
for bebida in bebidas:
    print(bebida)
