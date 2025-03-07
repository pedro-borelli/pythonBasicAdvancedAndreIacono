# Os laços de repetição em Python permitem que você execute um bloco de código várias vezes, dependendo de
# uma condição. Eles são fundamentais para automatizar tarefas repetitivas e são amplamente utilizados na programação.

# Tipos de laços de repetição em Python
# for: Repete sobre uma sequência (como lista, string, range) e executa o bloco de código para cada item da sequência.

#Sintaxe
# for item in sequencia:
 # Bloco de código a ser executado

# numa lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}.")

# com range
for numero in range(5):  # Gera números de 0 a 4
    print(numero)

# while: Repete o bloco de código enquanto uma condição for verdadeira.

#Sintaxe
# # while condicao:
#     # Bloco de código a ser executado

# contagem regressiva
contador = 5
while contador > 0:
    print(f"Contagem: {contador}")
    contador -= 1 # diminui o contador de 1 em 1 : 5,4,3,2,1...
print("Fim da contagem!")


# break: Encerra o laço imediatamente.

# break com while
contador = 0
while True:  # Loop infinito
    print(f"Contador: {contador}")
    contador += 1
    if contador == 5:  # Condição para parar o loop
        print("Saindo do loop.")
        break

# break com for
for numero in range(10):
    if numero == 6:  # Sai do loop quando o número for 6
        print("Encontrado número 6, saindo do loop.")
        break
    print(numero)


# continue: Interrompe apenas a iteração atual e passa para a próxima.
for i in range(5):
    if i == 3:
        continue  # Pula a iteração quando i é 3
    print(i)


