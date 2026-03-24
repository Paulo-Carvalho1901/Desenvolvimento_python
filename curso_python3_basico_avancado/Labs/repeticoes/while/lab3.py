# Exercício 2
# Imprima os números de **1 a 20** usando um `while`.

"""
Obs: muito importante lembrar sobre a influencia do print dentro do laço
se o print vem antes da iteração primeiro ele mostra o valor inicial no caso zero
se ele vem depois primeiro ele acumula depois ele mostra o resultado
"""
numero = 0

while numero < 21:
    print(numero)
    numero += 1

print('Fim...')