lista = []

# Append para juntar

lista.append(1)
lista.append("Python")
lista.append([40, 21, 60])
print(lista)

# Clear para limpar

lista.clear()
print(lista)

# Copy 
lista = [1, 2, 4 , 5, 6]
l2 = lista.copy()
print(l2)
print(id(l2), id(lista))

# Count - Utilizado para contar
cores = ["vermelho", "azul", "preto", "azul"]
cores.count("vermelho") # 1
cores.count("verde") # 0
cores.count("azul") # 2

# Extends - Juntar duas listas e adicionando no final
linguagens = ["python", "php", "javascrit", "code"]
print(linguagens)
linguagens.extend(["c#", "c"])
print(linguagens)

indexPython = linguagens.index("python")
indexPhP = linguagens.index("php")
indexC = linguagens.index("c#")
indexCSharp = linguagens.index("c")
print(indexPython)
print(indexPhP)
print(indexC)
print(indexCSharp)

# # POP
# linguagens.pop() # c
# linguagens.pop() # c#
# linguagens.pop() #code
# linguagens.pop(0) # python

# Remove, segunda forma de remover. Sempre passamos o objeto 
# linguagens.remove("php") # Removeu o php

# Reverse, pegar a lista e realizar um espelhamento

linguagens.reverse() 

#sort vai ordenar aleatoriamente a lista.
linguagens.sort() # organiza em ordem alfabetica
linguagens.sort(reverse=True) # organiza em ordem de tras para frente.
linguagens.sort(key=lambda x: len(x)) # Colocando em ordem do menor para o maior
linguagens.sort(key=lambda x: len(x), reverse=True) # Colocando em ordem do maior para o menor

# Len para saber o tamanho total da lista
len(linguagens) # Tamanho total da lista

# Sorted
sorted(linguagens, key=lambda x:len(x))
sorted(linguagens, key=lambda x:len(x), reverse=True)
print(sorted(linguagens)) # ['c', 'c#', 'code', 'javascrit', 'php', 'python']