"""
Repetições
while (enquanto)
Executa uma ação enquanto a condiçao for verdadeira
Loope infinito -> Quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input('Qual seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break # quebrando o laço

# print(123)
print('Acabou!')