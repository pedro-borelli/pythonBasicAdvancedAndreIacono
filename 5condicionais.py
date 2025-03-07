# Em Python, os condicionais permitem que o programa tome decisões com base em condições.
# A principal estrutura condicional é o if, que pode ser combinada com elif e else para tratar diferentes casos.

# Estrutura if:
# Executa um bloco de código se a condição for verdadeira (True).

idade = 18

if idade >= 18:
    print("Você é maior de idade.")  # Executado se a condição for verdadeira.

# Estrutura if-else:
# Inclui um bloco else que é executado quando a condição no if é falsa.

idade = 16

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")  # Executado se a condição for falsa.

# Estrutura if-elif-else
# Permite verificar múltiplas condições com elif (else if).
# O primeiro bloco elif verdadeiro será executado;
# se nenhum for verdadeiro, o bloco else será executado.

nota = 7

if nota >= 9:
    print("Ótimo desempenho!")
elif nota >= 7:
    print("Bom desempenho!")
elif nota >= 5:
    print("Aprovado com ressalvas.")
else:
    print("Reprovado.")

# Estrutura if Aninhado:
# Um if pode ser colocado dentro de outro if para tratar condições mais específicas.

idade = 20
tem_carteira = True

if idade >= 18:
    if tem_carteira:
        print("Pode dirigir.")
    else:
        print("Não pode dirigir sem carteira.")
else:
    print("Não pode dirigir por ser menor de idade.")

# Condicionais de Uma Linha (Ternário):
# Uma forma compacta de escrever if-else.

idade = 20
mensagem = "Maior de idade" if idade >= 18 else "Menor de idade"
print(mensagem)  # Saída: "Maior de idade"

# Usando Condicionais com Operadores Lógicos:
# Os operadores lógicos (and, or, not) são frequentemente usados para combinar condições.

idade = 20
altura = 1.75

if idade >= 18 and altura >= 1.60:
    print("Você está apto para o teste físico.")
else:
    print("Você não atende aos requisitos.")

# Condicionais com pass:
# Se você quiser um if que ainda não faz nada, pode usar o comando pass.

idade = 20

if idade >= 18:
    pass  # Placeholder, o código será implementado depois.
else:
    print("Menor de idade.")

