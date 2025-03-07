# Para este desafio, quero que você peça ao usuário que digite um
# número. Se o número for maior que 10, imprima 'O número é maior que 10'.
# Caso contrário, imprima 'O número é menor ou igual a 10'.

numero = int(input('Digite um número: '))
if numero > 10:
    print(f'{numero} é maior que 10. ')
else:
    print(f'{numero} é menor ou igual a 10.')
