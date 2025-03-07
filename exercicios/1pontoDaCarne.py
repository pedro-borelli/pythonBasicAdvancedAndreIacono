# criar um programa que dependendo da temperatura do steak ele retorna o ponto
# de cozimento. O usuário deverá fornecer a temperatura:

# temperaturas:
# 48ºC - Selada
# 54ºC - Ao ponto para o mal
# 60ºC - Ao ponto
# 65ºC - Ao ponto para o bem
# 71ºC - Bem passada

# Com range
# Solicita a temperatura da carne ao usuário
temperatura = int(input("Qual é a temperatura da carne? "))

# Determina o ponto de cozimento com base na temperatura
if temperatura in range(48):
    print("Selada")
elif temperatura in range(48, 54):
    print("Ao ponto para o mal")
elif temperatura in range(54, 60):
    print("Ao ponto")
elif temperatura in range(60, 65):
    print("Ao ponto para o bem")
elif temperatura in range(65, 71):
    print("Bem passada")
else:
    print("Queimada")