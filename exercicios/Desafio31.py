# Para este desafio, crie uma função lambda que aceite um número e
# retorne 'Par' se o número for par e 'Impar' se o número for impar.

num = int(input("Informe o número : "))

par_ou_impar = lambda verify: 'Par' if num % 2 == 0 else 'Impar'

print(par_ou_impar(num))