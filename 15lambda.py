# Uma função lambda é um conceito usado tanto na programação em geral quanto em serviços na nuvem, como o AWS Lambda.
# Abaixo explico os dois contextos:

# 1. Na Programação (Python)
# No contexto da programação, uma função lambda é uma função anônima, ou seja, uma função sem nome, que é geralmente
# usada para operações curtas e simples. Em Python, é definida com a palavra-chave lambda.

# Estrutura:
# lambda argumentos: expressão

# Exemplo:
# Função lambda para somar dois números
soma = lambda x, y: x + y
print(soma(3, 5))  # Saída: 8

# Função lambda em uma lista ordenada
nomes = ["Ana", "Carlos", "Beatriz"]
nomes_ordenados = sorted(nomes, key=lambda nome: len(nome))
print(nomes_ordenados)  # Saída: ['Ana', 'Carlos', 'Beatriz']

# Em Python, é possível fazer um if-else em uma função lambda usando a seguinte sintaxe:
# lambda argumentos: valor_se_verdadeiro if condicao else valor_se_falso

# As funções lambda são frequentemente usadas em contextos como ordenação, filtros, mapeamento e
# outras operações funcionais.


# 2. No Contexto da AWS (AWS Lambda)
# O AWS Lambda é um serviço de computação baseado em eventos fornecido pela Amazon Web Services (AWS).
# Ele permite que você execute código sem a necessidade de gerenciar servidores.
# Esse código, chamado de função Lambda, pode ser escrito em várias linguagens, como Python, Node.js, Java, etc.

