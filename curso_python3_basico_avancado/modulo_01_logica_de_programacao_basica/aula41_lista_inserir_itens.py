"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
lista.append("Paulo") # adicionei
nome = lista.pop() # Se passar o indice ele remove pelo indice, se não removi o ultimo item
lista.append(123)
del lista[-1] # deletando item pelo indice
# lista.clear() # limpando lista
lista.insert(0, 5) # lista.insert(qual indice, o valor do item)
# lista.insert(5, 'Paulo')
lista.insert(100, 50)
print(lista[5]) 
