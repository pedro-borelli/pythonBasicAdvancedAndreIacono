# As funções recursivas são funções que se chamam dentro do seu
# próprio bloco de código. Elas são úteis para resolver problemas que
# podem ser divididos em problemas menores de natureza semelhante.

# Um exemplo clássico de onde a recursão é usada é o cálculo do fatorial
# de um número. O fatorial de um número n é o produto de todos os números inteiros positivos
# de n até 1.

num = int(input('Informe o número fatorial:  '))


def calculo_fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * calculo_fatorial(num - 1)


print(calculo_fatorial(num))

