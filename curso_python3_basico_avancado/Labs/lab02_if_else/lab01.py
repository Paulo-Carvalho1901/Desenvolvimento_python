"""
Par ou Ímpar
Enunciado:
Peça um número inteiro ao usuário e diga se ele é par ou ímpar.
Exemplos

Entrada: 7 → Saída: Ímpar
Entrada: 12 → Saída: Par

Dica: use n % 2.
"""

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'Número {num} é par.')
else:
    print(f'Número {num} é impar.')
