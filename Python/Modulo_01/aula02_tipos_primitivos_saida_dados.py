# Tipos primitivos saida de dados

#  Saída de um input sempre será str

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
s = n1 + n2
# print('A soma entre', n1, 'e', n2, 'vale', s)
# função format()
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))
