"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Código sem fim
"""
condicao = True
while condicao:
    nome = input('Qual é o seu nome? ')
    print(f'Seu nome é {nome}')
    resp = input('Quer sair? [S para Sim]')
    if resp == 'S' or resp == 'Sim':
        break
print('Sim')