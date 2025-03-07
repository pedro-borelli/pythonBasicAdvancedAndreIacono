# Para este desafio, crie dois conjuntos, cada um contendo 5 nomes
# de seus amigos. Alguns nomes devem estar presentes em ambos os conjuntos.
# Use um método para encontrar quais nomes aparecem em ambos os conjuntos e imprima
# o resultado.

amigos1 = {'Rafael', 'Mallcon', 'Marcus', 'Antonio', 'Rodrigo'}
amigos2 = {'Rafael', 'Mallcon', 'Marcus', 'Larissa', 'Taiane'}

amigos_repetidos = amigos1.intersection(amigos2)
print(amigos_repetidos)
