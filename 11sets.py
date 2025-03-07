# Em Python, um set é uma coleção não ordenada de elementos únicos. Ele é usado para armazenar múltiplos itens
# em uma única variável, mas sem permitir duplicatas. Sets são definidos usando chaves {} ou pela função set().

# Principais operações e métodos de sets:
# Criar um set:
s = {1, 2, 3}
s2 = set([3, 4, 5])


# Métodos principais de manipulação:
# add: Adiciona um elemento ao set. Se o elemento já existir, ele será ignorado.
s.add(4)  # s agora é {1, 2, 3, 4}


# remove: Remove um elemento específico do set. Se o elemento não estiver presente, levanta um erro KeyError.
s.remove(2)  # s agora é {1, 3, 4}


# Operações entre sets:
# intersection: Retorna os elementos que estão presentes em ambos os sets (interseção).
s1 = {1, 2, 3}
s2 = {2, 3, 4}
inter = s1.intersection(s2)  # {2, 3}


# union: Retorna todos os elementos presentes em ambos os sets, eliminando duplicatas (união).
uniao = s1.union(s2)  # {1, 2, 3, 4}


# difference: Retorna os elementos que estão no set original, mas não no outro set (diferença).
diff = s1.difference(s2)  # {1}


# symmetric_difference: Retorna os elementos que estão em um dos sets, mas não em ambos (diferença simétrica).
sym_diff = s1.symmetric_difference(s2)  # {1, 4}