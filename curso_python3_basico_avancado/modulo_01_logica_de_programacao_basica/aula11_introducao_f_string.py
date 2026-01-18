# Introdução a f-strings que é um tipode formatação

nome = 'Paulo'
altura = 1.95
peso = 95
imc = peso / (altura * altura)

linha_01 = f'{nome} tem {altura:.2f} de altura'
linha_02 = f'{peso} quilos e seu IMC é'
linha_03 = f'{imc:.2f}'

print(linha_01)
print(linha_02)
print(linha_03)
