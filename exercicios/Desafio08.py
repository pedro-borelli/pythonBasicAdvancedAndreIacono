# Para este desafio, comece com a lista frutas do desafio anterior.
# Primeiro, seu desafio é alterar o segundo elemento da lista(indice 1) de banana
# para morango. Depois disso, adicione a fruta abacaxi ao final da lista. Por fim, imprima
# a lista modificada na tela.

frutas = ['maçã' , 'banana' , 'uva' ]

frutas.remove('banana')
frutas.insert(1,'morango')
frutas.insert(3, 'abacaxi')
print(frutas)