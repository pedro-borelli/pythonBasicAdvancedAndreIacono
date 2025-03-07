# Para este desafio, quero que você crie um loop que imprima
# os números de 1 a 10, mas pare de imprimir assim que chegar a 5
# usando o comando break. Em seguida, crie um segundo loop que imprima
# os números de 1 a 10, mas pule a impressão do número 5 usando o comando continue

# loop com break
for contador in range(1, 10, 1):
    if contador == 6: #para no numero 5
        print('Encontrado o valor de número 5, saindo do looping')
        break

    print(contador)

# loop com continue
for contagem in range(1, 10):
    if contagem == 5: #pula o numero 5
        continue
    print(contagem)
