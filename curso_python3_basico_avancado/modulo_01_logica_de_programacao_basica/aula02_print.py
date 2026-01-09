# \r\n => CRLF - quebra de linha
# \n => LF
print(12, 34, 1011, sep='-', end='##\n') # recebe um argumento, argumentos não-nomeados
print(56, 78, sep="-", end='\n') # recebe um argumento
print(9, 10, sep="-", end='\n') # recebe um argumento

# sep='' = separa os argumento não-nomeados
# end='' = altera o final da linha

# Print() função não definida
# preste atenção nos erros
# NameError: name 'Print' is not defined. Did you mean: 'print'?
