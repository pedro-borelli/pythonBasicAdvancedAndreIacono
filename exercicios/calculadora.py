def calculadora():
    print("Bem-vindo à Calculadora em Python!")
    print("Selecione a operação desejada:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    # Solicitar a operação do usuário
    escolha = input("Digite o número correspondente à operação (1/2/3/4): ")

    # Verificar se a escolha é válida
    if escolha in ['1', '2', '3', '4']:
        # Solicitar os números ao usuário
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")
            return

        # Realizar a operação escolhida
        if escolha == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif escolha == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida. Tente novamente.")

# Chamar a função da calculadora
calculadora()
