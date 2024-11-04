num1 = input('Digite o primeiro valor: ')
num2 = input('Digite o segundo valor: ')

if int(num1) > int(num2):
    print(num1, "é maior do que", num2)
elif num2 > num1:
    print(num2, "é maior do que", num1)
else:
    print(num1, " e ", num2, " tem o mesmo valor!")        