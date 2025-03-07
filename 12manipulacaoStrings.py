# Manipulação de strings em Python refere-se ao conjunto de operações que podemos realizar
# em textos (strings). Python oferece uma ampla gama de métodos embutidos para modificar,
# analisar, transformar e trabalhar com strings. Aqui estão os principais tópicos e exemplos:

# 1. Criando Strings
# Strings podem ser criadas com aspas simples (') ou duplas ("):
texto1 = 'Olá, Mundo!'
texto2 = "Python é incrível!"

# 2. Acessando Elementos
# Usamos índices para acessar caracteres:
texto = "Python"
print(texto[0])  # P
print(texto[-1])  # n (último caractere)

# 3. Fatiamento (Slicing)
# Obtenha partes da string:
texto = "Manipulação de Strings"
print(texto[0:12])  # 'Manipulação'
print(texto[13:])  # 'de Strings'
print(texto[:5])  # 'Manip'

# 4. Principais Métodos de Strings
# a. Alteração de Case (Maiúsculas/Minúsculas)
texto = "Python é Fantástico!"
print(texto.upper())  # 'PYTHON É FANTÁSTICO!'
print(texto.lower())  # 'python é fantástico!'
print(texto.capitalize())  # 'Python é fantástico!'
print(texto.title())  # 'Python É Fantástico!'


# 1. strip()
texto_strip = texto.strip()  # Remove espaços nas extremidades
print(f"strip(): '{texto_strip}'")  # Saída: 'Olá, Mundo!'

# 2. lstrip()
texto_lstrip = texto.lstrip()  # Remove espaços à esquerda
print(f"lstrip(): '{texto_lstrip}'")  # Saída: 'Olá, Mundo!   '

# 3. rstrip()
texto_rstrip = texto.rstrip()  # Remove espaços à direita
print(f"rstrip(): '{texto_rstrip}'")  # Saída: '   Olá, Mundo!'

# 4. rjust()
texto_rjust = texto_strip.rjust(20, '-')  # Preenche à esquerda para ter 20 caracteres
print(f"rjust(): '{texto_rjust}'")  # Saída: '----Olá, Mundo!'

# 5. ljust()
texto_ljust = texto_strip.ljust(20, '-')  # Preenche à direita para ter 20 caracteres
print(f"ljust(): '{texto_ljust}'")  # Saída: 'Olá, Mundo!----'

# 6. center()
texto_center = texto_strip.center(20, '-')  # Centraliza e preenche com '-'
print(f"center(): '{texto_center}'")  # Saída: '--Olá, Mundo!--'

# 7. replace()
texto_replace = texto_strip.replace("Mundo", "Python")  # Substitui "Mundo" por "Python"
print(f"replace(): '{texto_replace}'")  # Saída: 'Olá, Python!'

# 8. find()
indice = texto_strip.find("Python")  # Busca por "Python"
print(f"find(): {indice}")  # Saída: -1 (não encontrado)

# 9. split()
texto_split = texto_strip.split(",")  # Divide a string no caractere ","
print(f"split(): {texto_split}")  # Saída: ['Olá', ' Mundo!']

# 10. join()
texto_join = "-".join(texto_split)  # Junta as palavras com "-"
print(f"join(): '{texto_join}'")  # Saída: 'Olá-Mundo!'

# 11. isalpha() (verifica se a string contém apenas letras)
texto_alpha = "Python"
texto_num = "Python123"
print(f"isalpha() - '{texto_alpha}': {texto_alpha.isalpha()}")  # True
print(f"isalpha() - '{texto_num}': {texto_num.isalpha()}")    # False

# 12. isdigit() (verifica se a string contém apenas dígitos)
texto_digit = "12345"
print(f"isdigit() - '{texto_digit}': {texto_digit.isdigit()}")  # True

# 13. count()
contagem = texto_strip.count("Olá")  # Conta quantas vezes "Olá" aparece
print(f"count(): {contagem}")  # Saída: 2


# Diferença entre find() e index()
# Ambos buscam substrings e retornam o índice da primeira ocorrência.
# find() retorna -1 se a substring não for encontrada.
# index() gera um erro (ValueError) se a substring não for encontrada.

texto = "Python é divertido"

# find() não gera erro
print(texto.find("Java"))  # Saída: -1

# index() gera erro
print(texto.index("Java"))  # Gera ValueError