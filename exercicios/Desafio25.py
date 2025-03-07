# Para este desafio, crie uma função que aceite dois números como entrada
# e retorne a soma desses números.

num1 = float(input('Informe o primeiro valor: '))
num2 = float(input('Informe o segundo valor: '))

#função para somar
def soma(num1, num2):
    return num1 + num2


print(f' A soma de {num1} + {num2} é = {soma(num1, num2)}')
