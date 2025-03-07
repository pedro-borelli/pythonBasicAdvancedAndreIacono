# Em Python, dicionários são estruturas de dados que armazenam pares de chave-valor,
# permitindo acesso rápido aos valores associados a uma chave específica.
# Eles são definidos usando chaves {} e têm as seguintes características:

# Criar um dicionário vazio
meu_dicionario = {}

# Criar um dicionário com valores
meu_dicionario = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

# Criando um dicionário inicial
meu_dicionario = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "Rio de Janeiro"
}

# Acessando valores
print("Nome:", meu_dicionario["nome"])  # Acessar com a chave
print("Idade:", meu_dicionario.get("idade"))  # Acessar com get()

# Atualizando valores
meu_dicionario["idade"] = 31  # Atualizar o valor de 'idade'
meu_dicionario["profissão"] = "Designer"  # Adicionar nova chave-valor
print("\nDicionário atualizado:", meu_dicionario)

# Removendo valores
del meu_dicionario["cidade"]  # Remover a chave 'cidade'
profissao_removida = meu_dicionario.pop("profissão", "Chave não encontrada")  # Remover com pop()
print("\nApós remoções:", meu_dicionario)
print("Profissão removida:", profissao_removida)

# Listando todos os valores
print("\nUsando keys():", meu_dicionario.keys())  # Todas as chaves
print("Usando values():", meu_dicionario.values())  # Todos os valores
print("Usando items():", meu_dicionario.items())  # Todos os pares chave-valor

# Iterando sobre keys(), values() e items()
print("\nIterando sobre keys():")
for chave in meu_dicionario.keys():
    print(chave)

print("\nIterando sobre values():")
for valor in meu_dicionario.values():
    print(valor)

print("\nIterando sobre items():")
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")

