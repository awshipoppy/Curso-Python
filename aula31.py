"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e 
"""
# Mesmo valor puxa para mesmo lugar na memória
# v1 = 'a'
# v2 = 'a'
# print(id(v1))
# print(id(v2))

condicao = False
passou_no_if = None

# CÓDIGO ERRADO ------
# if condicao:
#     print('Faça algo')
#     passou_no_if = True
# else:
#     passou_no_if = None
#     print('Não faça algo')
# print(passou_no_if)

if condicao:
    print('Faça algo')
    passou_no_if = True
else:
    print('Não faça algo')
print(passou_no_if)
