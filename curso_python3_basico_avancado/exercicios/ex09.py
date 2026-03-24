# Calculadora com while

"""
sair = input('Quer sair? [s]im: ').lower().startswith('s')
nesse trecho estamos fazendo um vaerificação e tratando o que úsuario esta nos enviando

logo abaixo uma condição de parada break

"""


while True:
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    # sair = sair.lower()
    # sair = sair.startwith()
    
    if sair is True:
        break

