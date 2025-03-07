# Para este desafio, crie uma lista de frutas que inclui maçã
# tres vezes e outras frutas de sua escolha. Use um loop for
# para contar quantas vezes mação aparece na lista e imprima o resultado.

frutas = ['maçã', 'banana', 'maçã', 'manga', 'uva', 'maçã']
contador = 0

for fruta in frutas:
    if fruta == 'maçã':
        contador += 1

print(f"A palavra 'maçã' aparece {contador} vezes na lista.")
