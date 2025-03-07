# Para este desafio, crie uma função lambda que aceite dois números
# e retorne a multiplicação desses números.

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

multi = lambda x, y: num1 * num2

print(f'O resultado é : {multi(num1, num2)}')
