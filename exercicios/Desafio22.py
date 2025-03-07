# Para este desafio, crie uma lista com 5 nomes de países e as capitais
# desses países. Peça ao usuário para digitar o nome de um país. Se o país
# estiver na lista, imprima 'a capital de país é capital'. Se o país não estiver
# na lista, imprima 'Desculpe, não temos informações sobre a capital desse país'.

capitais = {
    'Brasil' : 'Brasília',
    'Argentina' : 'Buenos Aires',
    'Estados Unidos' : 'Washington',
    'Itália' : 'Roma',
    'Inglaterra' : 'Londres'
}

pais_usuario = input('Informe o país escolhido : ')

if pais_usuario in capitais:
    print(f' A capital do {pais_usuario} é {capitais[pais_usuario]} ')
else:
    print('Desculpe, não temos informações sobre a capital desse país')
