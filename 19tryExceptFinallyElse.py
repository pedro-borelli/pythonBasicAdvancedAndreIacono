# No Python, a estrutura try, except, finally e else é usada para lidar com exceções de maneira organizada.
# Aqui está o propósito de cada palavra-chave:

# 1. try
# O bloco try contém o código que pode gerar uma exceção. Se uma exceção ocorrer, o fluxo de execução passa
# para o bloco except.

# 2. except
# O bloco except é usado para capturar e tratar as exceções levantadas no bloco try.
# Você pode capturar exceções específicas ou genéricas.

# 3. else
# O bloco else é opcional e executa apenas se nenhuma exceção ocorrer no bloco try.

# 4. finally
# O bloco finally também é opcional e sempre é executado, independentemente de uma exceção ter sido levantada ou não.
# Ele é usado para liberar recursos, como fechar arquivos ou conexões.

# Sem erros:
try:
    print("Tentando dividir...")  # Saída: Tentando dividir...
    resultado = 10 / 2
except ZeroDivisionError as e:
    print("Erro: Divisão por zero não é permitida.")
else:
    print(f"Divisão bem-sucedida! Resultado: {resultado}")  # Saída: Divisão bem-sucedida! Resultado: 5.0
finally:
    print("Bloco finally sempre é executado.")  # Saída: Bloco finally sempre é executado.

# Com erro:
try:
    print("Tentando dividir...")  # Saída: Tentando dividir...
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Erro: {e}")  # Saída: Erro: division by zero
else:
    print("Isso não será executado, pois houve um erro.")
finally:
    print("Bloco finally sempre é executado.")  # Saída: Bloco finally sempre é executado.