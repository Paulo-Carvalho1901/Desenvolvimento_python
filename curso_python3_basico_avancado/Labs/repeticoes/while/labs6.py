# Uma situação comum: o programa só continua quando o usuário digita a senha correta.

senha_secreta = '1234'
senha = ''

while senha != senha_secreta:
    senha = input('Digite sua senha: ')

print('Acesso permitido.')
