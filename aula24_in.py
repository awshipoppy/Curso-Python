# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# O t á v i o
#-6-5-4-3-2-1
nome = 'Otávio'
# print(nome[2])
# print('á' in nome)
# print('z' in nome)
# print(15 * '=')
# print('Ot' not in nome)
# print('Zika' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')