"""
Faça um programa que pergunte a hora ao úsuario e, baseando-se no horario
descrito, exiba a saudação apropriada ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

hora_dia = input('Digite a hora do dia: ')

hora_dia_int = int(hora_dia)

if hora_dia_int >= 0 and hora_dia_int <= 11:
    print('BOM DIA')
elif hora_dia_int >= 12 and hora_dia_int <= 17:
    print('BOA TADE')
elif hora_dia_int >= 18 and hora_dia_int <= 23:
    print('BOA NOITE')
else:
    print('Você não digitou uma hora valida.')
