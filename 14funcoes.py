# Componentes
# def: Palavra-chave para definir uma função.
# nome_da_funcao: Nome da função, usado para chamá-la.
# parametros: Valores que a função pode receber como entrada.
# return: (Opcional) Retorna um resultado da função.

# Function (Função)
# Definição: Um bloco de código reutilizável que executa uma tarefa específica.
# Uso: Ajuda a modularizar e reutilizar código.
# Exemplo (Python):
def somar(a, b):
    return a + b


print(somar(2, 3))  # Saída: 5


# ---------------------------------------------------------------------------------------

# Module (Módulo)
# Definição: Um arquivo Python contendo código (funções, classes, etc.) que pode ser importado e reutilizado.
# Uso: Divide o código em partes menores e organizadas.

# Exemplo:
# Arquivo meu_modulo.py:
def saudacao(nome):
    return f"Olá, {nome}!"


# Uso no programa principal:
# import meu_modulo
# print(meu_modulo.saudacao("João"))  # Saída: Olá, João!


# ----------------------------------------------------------------------------------------
# Package (Pacote)
# Definição: Uma coleção de módulos organizados em diretórios.
# É um diretório contendo um arquivo __init__.py (pode estar vazio) e módulos associados.
# Uso: Organiza módulos relacionados em uma estrutura hierárquica.
# Exemplo:
# Estrutura:
# markdown
# meu_pacote/
#     __init__.py
#     modulo1.py
#     modulo2.py
# Uso:
# from meu_pacote import modulo1

# ------------------------------------------------------------------------------------------
# Library (Biblioteca)
# Definição: Um conjunto de módulos e/ou pacotes prontos para uso, geralmente fornecendo funcionalidades para tarefas
# específicas.
# Uso: Ferramentas reutilizáveis criadas por terceiros ou pela comunidade.
# Exemplo:
# Biblioteca math:
import math

print(math.sqrt(16))  # Saída: 4.0


# Resumo das Relações:
# Funções são blocos de código.
# Módulos contêm funções e/ou classes.
# Pacotes organizam múltiplos módulos.
# Bibliotecas são coleções de pacotes/módulos prontos para uso.


# Função default: Função onde todos os parâmetros possuem valores padrão. Permite chamada sem argumentos.

def saudacao(msg ="Olá"):
    return msg

# Função non-default:	Função que exige argumentos específicos, pois não há valores padrão definidos.
def soma(a, b):
    return a + b

# Combinação em uma função:
# É permitido misturar parâmetros default e non-default, mas os default devem vir por último:
def exemplo(a, b=10):  # 'a' é non-default, 'b' é default
    return a + b

