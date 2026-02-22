"""
Multa de Velocidade
Enunciado:
Leia a velocidade do carro (km/h). Se for maior que 80, exiba Multado! e calcule a multa como R$ 7,00 por km acima de 80. 
Caso contrário, exiba Dentro do limite.
Exemplos

Entrada: 75 → Saída: Dentro do limite
Entrada: 90 → Saída: Multado! Valor: R$ 70.00

Dica: multa = (vel - 80) * 7.
"""

# Definindo variaveis importantes
valocidade = input('A velocidade foi: ')
multa = (int(valocidade) - 80) * 7

valocidade_int = int(valocidade)

if valocidade_int > 80:
    print(f'Você foi multado, sua multa será de R${multa:.2f} reis.')
elif valocidade_int <= 80:
    print('Dentro do limite de velocidade!')
