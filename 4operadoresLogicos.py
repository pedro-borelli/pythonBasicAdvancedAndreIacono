# Os operadores lógicos em Python são usados para combinar expressões ou valores booleanos e
# determinar o resultado com base em condições lógicas. Eles retornam True ou False dependendo da lógica aplicada.

# and (E lógico):
# Retorna True se ambas as condições forem verdadeiras. Caso contrário, retorna False.
a = 10
b = 20
print(a > 5 and b > 15)  # True (ambas as condições são verdadeiras)
print(a > 15 and b > 15) # False (a > 15 é falso)

# or (OU lógico):
# Retorna True se pelo menos uma das condições for verdadeira. Caso todas sejam falsas, retorna False.
a = 10
b = 20
print(a > 5 or b > 25)  # True (a > 5 é verdadeiro)
print(a > 15 or b > 25) # False (ambas as condições são falsas)

# not (Negação lógica)
# Inverte o valor lógico da condição. Se for True, retorna False, e vice-versa.
a = 10
print(not a > 5)  # False (a > 5 é verdadeiro, mas `not` inverte para falso)
print(not a > 15) # True (a > 15 é falso, mas `not` inverte para verdadeiro)

