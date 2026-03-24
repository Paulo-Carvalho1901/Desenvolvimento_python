# nome = 'Paulo'

# indice = 0
# novo_nome = ''

# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'-{letra}'

#     indice += 1

# novo_nome += '-'
# print(novo_nome)

# Exercício 1
# Peça para o usuário digitar números até que ele digite **0**. Ao final, exiba a soma de todos os números digitados.

soma = 0
numero = int(input('Digite um número digite "0" para sair: '))

while numero != 0:
    soma += numero
    numero = int(input('Digite um número digite "0" para sair: '))

print(f'A soma dos números diggitados é: {numero}')

