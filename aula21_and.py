# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas a condições precisam ser verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy
# Também existe o tipo None que é
# usado para representar um não valor
entrada = input('[E] Entrar [S] Sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')