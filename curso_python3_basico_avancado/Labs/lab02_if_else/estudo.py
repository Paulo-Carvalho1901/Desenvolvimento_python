# Estruturas Condicionais em Python

# As estruturas condicionais são fundamentais em qualquer linguagem de programação, pois permitem tomar
# decisões com base em condições lógicas. Em Python, trabalhamos principalmente com:

# if
# elif
# else

# Este guia traz explicações claras, exemplos, boas práticas e pegadinhas comuns.

# 1. O que é uma condição?
# Uma condição é uma expressão que avalia para Verdadeiro (True) ou Falso (False).
# Em Python, além de True e False, outros valores também são considerados verdadeiros ou falsos.

# Valores Falsy (tratados como False):
# False
# 0 (de qualquer tipo numérico)
# None
# "" (string vazia)
# [] (lista vazia)
# {} (dicionário vazio)
# set() (conjunto vazio)

# Valores Truthy (tratados como True):
# Quase tudo que não estiver na lista acima.

# 2. Estrutura básica do if

# if condição:
    # bloco executado se condição for verdadeira

# Exemplo:

# idade = 20
# if idade >= 18:
#     print("Maior de idade")

# 3. Estrutura completa: if, elif, else

x = 10

if x > 10:
    print("Maior que 10")
elif x == 10:
    print("Igual a 10")
else:
    print("Menor que 10")

# Regras importantes
# Pode haver vários elif
# Só pode existir um else, ao final
# A indentação é obrigatória (4 espaços é o padrão)

