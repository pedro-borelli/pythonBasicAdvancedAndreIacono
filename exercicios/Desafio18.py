# Para este desafio, imagine que você tem uma loja de carros.
# Crie uma lista com os carros que você tem em estoque: BMW X6, BMW I5,
# BMW I8. Peça ao usuário para que ele insira o nome do carro que deseja
# comprar. Se o carro estiver em estoque, imprima 'Este carro está disponível'.
# Se o carro não estiver em estoque, imprima 'Desculpe, este carro não está disponível'.

carros = ['BMW X6' , 'BMW I5' , 'BMW I8']
modelo = input('Insira o nome do modelo de carro que deseja: ')

if modelo in list(carros):
    print(f'Este carro {modelo} está disponível')
else:
    print(f'Desculpe, este carro não está disponível')
