# Neste desafio, quero que você crie um script que pergunte o
# nome e a idade do usuário, usando a função input(). Depois
# disso, o script deve imprimir uma mensagem que diga 'Olá,
# [nome]! Você tem [idade] anos'.

nome = str(input('Qual é o seu nome? '))
idade = int(input('Qual é a sua idade? '))

print( f' Olá, {nome} ! Você tem {idade} anos. ')