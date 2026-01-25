# if / elif      / else
# se / se não se / se não

"""
- Utilizado para muda o fluxo do seu código
"""

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar': # Esse trecho só será executado se for verdadeiro
    print('Voce entrou do sistema!')
    print(133) # podendo ter varias linhas de código!
elif entrada == 'sair':
    print('Voce saiu do sistema!')
else:
    print('Você não digitou nem entrar nem sair.')

print('FORA DOS BLOCOS!')
