# SyntaxError:	Ocorre quando o código não segue a sintaxe do Python.
# IndentationError:	Ocorre quando a indentação está ausente ou incorreta.
# NameError:	Ocorre quando uma variável ou função não foi definida.
# TypeError:	Ocorre quando uma operação é aplicada a um tipo de dado incompatível.
# ValueError:	Ocorre quando uma função recebe um valor inválido, mas o tipo está correto.
# IndexError:	Ocorre quando você tenta acessar um índice que não existe em uma lista ou sequência.
# KeyError:	Ocorre quando você tenta acessar uma chave que não existe em um dicionário.
# AttributeError:	Ocorre quando você tenta acessar um atributo que não existe em um objeto.
# ImportError:	Ocorre quando o Python não consegue importar um módulo.
# ZeroDivisionError:	Ocorre ao tentar dividir um número por zero.
# FileNotFoundError:	Ocorre quando você tenta acessar um arquivo que não existe.
# RuntimeError:	Erro genérico que ocorre durante a execução do programa.
# MemoryError:	Ocorre quando o programa tenta usar mais memória do que o disponível.
# UnboundLocalError:	Ocorre quando você tenta usar uma variável local antes de inicializá-la.
# IndentationError:	Erro de indentação, comum ao usar espaços e tabulações misturados.



# 1. SyntaxError (comentado, pois interrompe a execução do programa imediatamente)
# if True print("Erro de sintaxe!")  # Falta dos dois pontos (:)

# 2. IndentationError
# def funcao():
# print("Sem indentação!")  # O código não está corretamente indentado
variavel_nao_definida = 0
try:
    # 3. NameError
    print(variavel_nao_definida)  # Variável não foi definida
except NameError as e:
    print(f"Erro: {e}")

try:
    # 4. TypeError
    print("Número: " + 5)  # Tentativa de concatenar string com inteiro
except TypeError as e:
    print(f"Erro: {e}")

try:
    # 5. ValueError
    numero = int("abc")  # Conversão inválida de string para inteiro
except ValueError as e:
    print(f"Erro: {e}")

try:
    # 6. IndexError
    lista = [1, 2, 3]
    print(lista[5])  # Índice fora do intervalo
except IndexError as e:
    print(f"Erro: {e}")

try:
    # 7. KeyError
    dicionario = {"a": 1}
    print(dicionario["b"])  # Chave inexistente
except KeyError as e:
    print(f"Erro: {e}")

try:
    # 8. AttributeError
    numero = 5
    numero.append(10)  # Inteiros não possuem o método append
except AttributeError as e:
    print(f"Erro: {e}")

try:
    # 9. ImportError
    import modulo_inexistente  # Tentativa de importar um módulo inexistente
except ImportError as e:
    print(f"Erro: {e}")

try:
    # 10. ZeroDivisionError
    resultado = 10 / 0  # Divisão por zero
except ZeroDivisionError as e:
    print(f"Erro: {e}")

try:
    # 11. FileNotFoundError
    arquivo = open("arquivo_inexistente.txt", "r")  # Arquivo não encontrado
except FileNotFoundError as e:
    print(f"Erro: {e}")

try:
    # 12. RuntimeError
    def recursao_infinita():
        return recursao_infinita()
    recursao_infinita()  # Recursão infinita
except RuntimeError as e:
    print(f"Erro: {e}")

try:
    # 13. MemoryError
    lista = [1] * (10**10)  # Tenta alocar mais memória do que o disponível
except MemoryError as e:
    print(f"Erro: {e}")

# try:
    # 14. UnboundLocalError
#     def funcao():
#         print(x)  # Variável usada antes de ser definida
#         x = 5
#     funcao()
# except UnboundLocalError as e:
#     print(f"Erro: {e}")

# 15. IndentationError (comentado, pois interrompe a execução do programa imediatamente)
# def outra_funcao():
# print("Indentação errada!")
