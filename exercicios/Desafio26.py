# Para este desafio, crie uma função que calcule a potência de um número.
# A função deve aceitar dois argumentos: a base e o expoente. No entanto,
# se o expoente não for fornecido ao chamar a função, ele deve assumir o valor
# padrão de 2.

def potencia(base, expoente=2):
    return base ** expoente

base = int(input('Qual é o valor da base? '))
expoente = (input('Qual é o valor do expoente? (default: 2) : '))

if expoente:
    print(f'O resultado é : {potencia(base, int(expoente))}')
else:
    print(f'O resultado é: {potencia(base)}')
