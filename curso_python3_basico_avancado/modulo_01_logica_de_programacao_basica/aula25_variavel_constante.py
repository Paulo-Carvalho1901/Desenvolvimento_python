"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

valocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and valocidade_carro_passou_radar_1

# ele passou no radar
if valocidade_carro_passou_radar_1:
    print('Velocidade do carro passou radar 1.')

if carro_passou_radar_1:
    print('Carro pasou radar 1')

# Verificando se foi multado
if carro_multado_radar_1:
    print('Carro multado em radar 1.')
