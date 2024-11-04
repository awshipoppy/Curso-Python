"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + 
Ex.: 0>-100, 1.f
Conversation flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:->10}')
print(f'{variavel:-<10}')
print(f'{variavel:-^10}')
print(f'{12123.12121821928121:.2f}')


