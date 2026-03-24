"""
Repetições
while (enquanto)
Executa uma ação enquanto a condiçao for verdadeira
Loope infinito -> Quando um código não tem fim
"""

qtd_linha = 5
qtd_coluna = 5

linha = 1
while linha <= qtd_linha: # laço externo
    coluna = 1
    while coluna <= qtd_coluna: # laça interno
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou!')
