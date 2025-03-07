# Em Python, separadores são caracteres ou símbolos usados para separar valores em uma linha de código.
# Eles aparecem em vários contextos, como impressão de valores, manipulação de strings, ou ao definir listas e tuplas.

# print: Na função print(), o parâmetro sep define o separador usado entre os valores ao exibi-los.

# Usando espaço como separador padrão
print("Python", "é", "incrível!")  # Saída: Python é incrível!

# Alterando o separador para um hífen
print("Python", "é", "incrível!", sep="-")  # Saída: Python-é-incrível!

# Separador com símbolos
print("2024", "12", "06", sep="/")  # Saída: 2024/12/06

#O método split(): divide uma string com base em um separador.

texto = "Python,Java,C++"
linguagens = texto.split(",")  # Divide a string onde há vírgulas
print(linguagens)  # Saída: ['Python', 'Java', 'C++']

# O método join() une elementos de uma lista em uma string, usando um separador.

linguagens = ["Python", "Java", "C++"]
texto = ", ".join(linguagens)  # Junta os elementos com ", " como separador
print(texto)  # Saída: Python, Java, C++

# format():é um método em Python usado para formatar strings, permitindo inserir valores em locais específicos de
# uma string com marcadores de posição. Ele é flexível e fácil de usar, permitindo criar saídas personalizadas.

# Sintaxe Básica: Os valores entre {} são os marcadores de posição, e o método format() insere os valores fornecidos
# nos respectivos lugares.

valor1 = 7
valor2 = 19

template = "Texto com {} e {}."
resultado = template.format(valor1, valor2)
print(resultado)

# Casas Decimais Você pode especificar o número de casas decimais com :.nf.

pi = 3.14159265
print("O valor de Pi é aproximadamente {:.2f}.".format(pi))  # Saída: O valor de Pi é aproximadamente 3.14.

# f-strings: Com elas, você pode incluir expressões diretamente dentro de chaves {} em uma string prefixada com f.

# Para criar uma f-string, basta adicionar o prefixo f antes da string e usar {} para incluir expressões ou variáveis.
nome = "Alice"
idade = 25
print(f"Meu nome é {nome} e eu tenho {idade} anos.")
# Saída: Meu nome é Alice e eu tenho 25 anos.

# diferenças de format para f-string:

# Usando format()
nome = "Ana"
idade = 23
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))

# Usando f-strings
print(f"Meu nome é {nome} e eu tenho {idade} anos.")



