frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

i = 0
apareceu_mais = 0
letra_que_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    letras_repetidas = frase.count(letra_atual)

    if apareceu_mais < letras_repetidas:
        apareceu_mais = letras_repetidas
        letra_que_apareceu_mais_vezes = letra_atual

    i += 1
print(f'A letra que apareceu mais vezes foi {letra_que_apareceu_mais_vezes} e foi {apareceu_mais}')