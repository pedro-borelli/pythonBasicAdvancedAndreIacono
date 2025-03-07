# criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário deverá
# fornecer as seguintes informações: rendimento, altura e largua.O programa deve mostrar na tela a mensagem
# 'Você necessita de X latas de tinta'


# Solicita os valores ao usuário
rendimento = float(input('Qual é o rendimento da lata de tinta? '))
altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largua da parede: '))

# Função para calcular a quantidade de tinta necessária
def quantidade_tinta():
    area = altura * largura
    total = area / rendimento
    print(f'Você necessita de {total:.2f} tintas')

#Exibir na tela o resultado
quantidade_tinta()
