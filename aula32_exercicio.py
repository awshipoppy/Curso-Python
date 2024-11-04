"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print("Primeiro Exercício ---")
print(end='\n\n\n')
num = int(input("Digite um número inteiro: "))



# Verifica se o número é par ou ímpar
if num % 2 == 0:
    print(f"{num} é um número par")
else:
    print(f"{num} é um número ímpar")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print("Segundo Exercício ---")
print(end='\n\n\n')

# Perguntando as horas
hora = int(input('Qual são as horas? Exemplo: 12 para 12h: '))
minu = int(input('Quais são os minutos? Exemplo: 25 para 25m: '))

# Concatenando os horários
relogio = str(hora) + ':' + str(minu)

# Lógica dos horários
if hora <= 11:
    print(f'Bom dia, são {relogio}')
elif hora >= 12 and hora <= 17:
    print(f'Boa tarde, são {relogio}')
elif hora <= 23:
    print(f'Boa noite, são {relogio}')
else:
    print(f'Horário não permitido')
    

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print("Terceiro Exercício ---")
print(end='\n\n\n')
nome = input('Digite o seu nome: ')
num_nome = len(nome)

if num_nome <= 4:
    print('Seu nome é curto')
elif num_nome == 5 or num_nome == 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')

