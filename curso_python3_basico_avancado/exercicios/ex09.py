# Calculadora com while

"""
sair = input('Quer sair? [s]im: ').lower().startswith('s')
nesse trecho estamos fazendo um vaerificação e tratando o que úsuario esta nos enviando

logo abaixo uma condição de parada break

"""


while True:
    # solicitando os dados para úsuario
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None # Bandeira (flag)

    # Aqui um ponto importante, poderia no lugar de try, except 
    # utilizar isdigit() para validar se que o úsuario enviou é realmente um número

    # tratando erros
    try:
        numero_1_flot = float(numero_1)
        numero_2_flot = float(numero_2)
        numeros_validos = True # se chegar aqui quer dizer que os números são validos
    except:
        numeros_validos = None

    # condição nessa condição checa, se os números são validos 
    # se os números forem iguais ao None é números são invalidos
    if numeros_validos is None:
        print('Um ou ambos os números digitados não são validos.')
        continue # volta no inicio pedindo para solicitar os números novamente

    operadores_permitidos = '+-/*'

    # Aqui testa a condição se o operador operador nao esta em operador_permitidos
    # se o valor não estiver "operadores permitidos"
    if operador not in operadores_permitidos:
        print('Operador invalido.')
        continue # volta no inicio pedindo para solicitar os números novamente

    # Aqui testa a lógica se tamanho do operador > 1
    # digite apenas 1 operador garantindo essa condição
    if len(operador) > 1:
        print('Digite apenas 1 operador')
        continue # volta no inicio pedindo para solicitar os números novamente

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break # para o laço while quando "sair" for True

