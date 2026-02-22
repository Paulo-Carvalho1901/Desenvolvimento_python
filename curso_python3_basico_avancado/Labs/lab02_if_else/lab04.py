"""
Ano Bissexto (simplificado)
Enunciado:
Peça um ano e diga se ele é bissexto seguindo a regra:

É bissexto se for divisível por 4 e não por 100, ou se for divisível por 400.

Exemplos

Entrada: 2024 → Saída: Bissexto
Entrada: 1900 → Saída: Não bissexto
Entrada: 2000 → Saída: Bissexto

Dica: combine condições com and e or.

"""

ano = int(input('Digite o ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('bissexto')
else:
    print('Não bissexto')


def eh_bissexto(ano: int) -> bool:
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Exemplos de uso:
testes = [2024, 1900, 2000, 2023, 2400]
for a in testes:
    print(a, "→", "Bissexto" if eh_bissexto(a) else "Não bissexto")
