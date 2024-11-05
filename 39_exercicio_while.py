"""
Iterando strings com while
"""
#       012345678910
nome = 'Carol Amor Amor Amor' # Iteráveis

tamanho_nome = int(len(nome))
print(nome)
print(tamanho_nome)
print(nome[3])

contador = 0

novo_nome = ''
while contador < tamanho_nome:
    novo_nome = novo_nome + nome[contador] + '*'
    contador += 1
print(novo_nome)