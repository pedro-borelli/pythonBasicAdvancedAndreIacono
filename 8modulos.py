# O Python vem com uma biblioteca padrão rica, composta por vários módulos que
# ajudam em diversas tarefas como manipulação de arquivos, operações matemáticas,
# manipulação de datas, acesso à internet, e mais.

# Aqui estão os principais módulos do Python agrupados por categorias:

# 1. Módulos para Manipulação de Dados
# math: Fornece funções matemáticas básicas e avançadas.
import math
print(math.sqrt(16))  # Raiz quadrada
print(math.pi)        # Valor de PI

# random: Gera números aleatórios e embaralha sequências.
import random
print(random.randint(1, 10))  # Número inteiro aleatório

# statistics: Realiza cálculos estatísticos básicos.
import statistics
print(statistics.mean([1, 2, 3]))  # Média

# decimal: Trabalha com números decimais de alta precisão.
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))

# fractions: Manipula frações matemáticas.
from fractions import Fraction
print(Fraction(1, 3) + Fraction(2, 3))  # Resultado: 1/1


# 2. Módulos para Datas e Horas
# datetime: Manipula datas e horários.
from datetime import datetime
print(datetime.now())  # Data e hora atual

# time: Lida com o tempo e pausas no código.
import time
time.sleep(2)  # Pausa por 2 segundos

# calendar: Trabalha com calendários e anos.
import calendar
print(calendar.month(2023, 12))  # Calendário de dezembro de 2023


# 3. Módulos para Manipulação de Arquivos
# os: Interage com o sistema operacional.
import os
print(os.listdir())  # Lista arquivos do diretório atual

# shutil: Realiza operações de arquivos e diretórios, como cópia e remoção.
import shutil
shutil.copy("arquivo.txt", "copia.txt")

# pathlib: Lida com caminhos de arquivos de forma moderna.
from pathlib import Path
caminho = Path("arquivo.txt")
print(caminho.exists())  # Verifica se o arquivo existe

# json: Trabalha com dados no formato JSON.
import json
data = {"nome": "Alice", "idade": 25}
print(json.dumps(data))  # Converte para string JSON

# csv: Lida com arquivos CSV.
import csv
with open("dados.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Idade"])


# 4. Módulos para Redes e Web
# requests (externo): Faz requisições HTTP.
import requests
response = requests.get("https://api.github.com")
print(response.status_code)

# http: Cria e manipula servidores HTTP.
from http.server import SimpleHTTPRequestHandler

# socket: Trabalha com redes em baixo nível.
import socket


# 5. Módulos para Desenvolvimento
# argparse: Lida com argumentos de linha de comando.
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--nome", help="Informe o nome")
args = parser.parse_args()

# logging: Registra mensagens para depuração e monitoramento.
import logging
logging.warning("Este é um aviso!")

# unittest: Cria testes para código Python.
import unittest


# 6. Módulos de Segurança
# hashlib: Cria hashes de dados (MD5, SHA256, etc.).
import hashlib
hash = hashlib.sha256(b"texto").hexdigest()
print(hash)

# secrets: Gera números e strings aleatórios seguros.
import secrets
print(secrets.token_hex(16))  # Token seguro


# 7. Módulos para Ciências de Dados
# numpy (externo): Manipulação de arrays numéricos.
# pandas (externo): Análise e manipulação de dados tabulares.
# matplotlib (externo): Criação de gráficos.


# 8. Módulos Diversos
# sys: Acessa funcionalidades do interpretador Python.
import sys
print(sys.version)  # Versão do Python

# re: Trabalha com expressões regulares.
import re
print(re.match(r"\d+", "123abc"))  # Encontra números no início da string

# itertools: Cria combinações e iteradores eficientes.
import itertools
print(list(itertools.permutations([1, 2, 3])))