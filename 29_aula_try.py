"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

num_str = input(
    'Vou dobrar o número que você digitar: '
)

try:
    num_float = float(num_str)
    print('FLOAT: ', num_float)
except:
    print('Isso não é um número')
