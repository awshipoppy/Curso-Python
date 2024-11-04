nome = 'José Filipe'
altura = 1.90
peso = 80.45
imc = peso / (altura * altura)

# Feito para juntar tudo em apenas uma string
# Chamada de f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso:.2f} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

# Jeito certo
print(linha_1)
print(linha_2)
print(linha_3)