"""
Faça um programa que peça ao úsuario para digitar um número inteiro,
informe se este número é par ou impar. Caso o úsuario não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input('Digite um número: ')

# numero_int = int(numero)

# if numero.isdigit():
#     if numero_int % 2 == 0:
#         print(f'Seu número digitado "{numero_int}" é PAR...')
#     else:
#         print(f'Seu número digitado "{numero_int}" IMPAR...')
# else:
#     print('Favor digite apenas números inteiros.')

# Outra solução


numero = input('Digite um número: ')

if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'Seu número digitado "{numero_int}" é PAR...')
    else:
        print(f'Seu número digitado "{numero_int}" IMPAR...')
else:
    print('Favor digite apenas números inteiros.')
