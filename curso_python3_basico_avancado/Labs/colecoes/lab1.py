# listas - declarando uma lista

lista = [10, 20, 30, 40]
print(lista)
# Uma lista é uma estrutura de dados mutavel, ou seja pode ser alterada

# alterando o valor de uma lista pelo seu indice
lista[1] = 200
print('Lista valor modificado', lista)

# podemos tambem em uma lista deletar um valor pelo indice
del lista[-1] # utimo valor
print(lista)

# podemos também add valores com append
lista.append(70)
print('Adicionado valor na lista', lista)

# podemos tambem retirar um valor da lista com pop
ultimo_valor = lista.pop()
print('Valor pego pelo pop',ultimo_valor, lista)

# como voce ve remove o ultimo valor inserido na lista