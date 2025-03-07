# Para este desafio, crie uma função lambda que eleve um número ao
# quadrado. Em seguida, use essa função para calcular o quadrado de todos os números
# em uma lista usando um loop for.

numList = [1, 2, 3, 4, 5, 6]

calculo_lista = lambda lista: [num ** 2 for num in lista]

print(calculo_lista(numList))
