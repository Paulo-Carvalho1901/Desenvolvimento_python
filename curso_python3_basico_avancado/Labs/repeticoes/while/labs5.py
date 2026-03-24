"""
Imagine que você está em uma fila de atendimento, como em um banco. Você pega sua senha e espera até
que o painel chame o seu número.

Isso parece muito com um loop while: o sistema continua chamando números enquanto o número atual
"""

from time import sleep

minha_senha = 25
senha_atual = 1

print('Aguardando sua senha ser chamada.')

while senha_atual != minha_senha:
    sleep(1)
    print(f'Chamando senha {senha_atual}...')
    senha_atual += 1

print('Sua senha foi chamada!, dirijase ao atendimento.')
