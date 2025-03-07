# Para este desafio, crie duas funções. A primeira função deve aceitar
# um número e retornar o dobro desse número. A segunda função deve aceitar
# um número e retornar o quadrado desse número. Em seguida, chame a primeira
# função dentro da segunda para retornar o quadrado do dobro de um número.

num1 = int(input('Informe o número: '))


def dobro():
    return num1 * 2


def quadrado():
    return dobro() ** 2


print(f'O quadrado do dobro desse número é {quadrado()}')
