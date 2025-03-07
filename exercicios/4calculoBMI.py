# Crie um programa que calcule o IMC - Indice de Massa Corporal

# Interpretação dos Resultados (Padrão da OMS):
# Menor que 18.5: Abaixo do peso
# 18.5 a 24.9: Peso normal
# 25 a 29.9: Sobrepeso
# 30 a 34.9: Obesidade Grau I
# 35 a 39.9: Obesidade Grau II
# 40 ou mais: Obesidade Grau III (mórbida)

# criando as variáveis
peso = float(input('Informe o valor do seu peso (kg): '))
altura = float(input('Informe sua altura (m): '))
massa_corporal = peso / (altura ** 2)


# executando a lógica
if massa_corporal < 18.5:
    print('Abaixo do peso')
elif 18.5 <= massa_corporal < 25:
    print('Peso Normal')
elif 25 <= massa_corporal < 30:
    print('Sobrepeso')
elif 30 <= massa_corporal < 35:
    print('Obesidade Grau I')
elif 35 <= massa_corporal < 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Mórbida')



