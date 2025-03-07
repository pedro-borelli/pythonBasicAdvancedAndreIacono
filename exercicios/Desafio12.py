# Para este desafio, crie uma lista de frutas e outra de vegetais.
# Use um for loop aninhado (nested for loop) para imprimir todas
# as combinações possíveis de frutas e vegetais, com a fruta primeiro
# e o vegetal em segundo.

frutas = ['maçã', 'banana', 'maracujá']
vegetais = ['brócolis', 'alface', 'rucula']

for fruta in frutas: #loop externo
    for vegetal in vegetais: #loop interno
        print(f'{fruta} e {vegetal}')

