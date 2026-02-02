"""
Maioridade
Enunciado:
Peça a idade do usuário e informe:

Menor de idade (menos de 18)
Maior de idade (entre 18 e 64)
Idoso (65 ou mais)

Exemplos

Entrada: 17 → Saída: Menor de idade
Entrada: 65 → Saída: Idoso

Dica: compare com >= e <.
"""

idade = int(input('Digite sua idade: '))

if idade <= 17:
    print('Menor de idade')
elif idade >= 18 and idade <= 64:
    print('Maior de idade')
elif idade >= 65:
    print('Idoso')
else:
    print('Digite apenas númemros inteiros')