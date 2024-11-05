# Interpolação básica de strings
# s - string 
# d e i - int
# f - float
# x e X - Hexadecimal

nome = 'Luiz'
preco = 1000.95
variavel = '%s, o preço é R$ %.2f' % (nome, preco)
print(variavel)
numero = 10329124
print('O hexadecimal de %d é %05x' % (numero, numero))
