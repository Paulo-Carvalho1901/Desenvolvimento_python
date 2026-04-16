"""
Iterável ->, range str, etc (__inier__)
iterador -> quem sabe entregar um valor por vez
next -> me entrega o proximo valor
iter -> me entrega o seu iterador
"""

# entendendo como for funciona
# texto = iter('Paulo') # __iter__()

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

# exeplo pratico de como funciona

texto = 'Paulo' # iterável
iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration: 
        break
