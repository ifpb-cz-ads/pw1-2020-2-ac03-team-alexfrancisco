
num1 = float(input('Informe um numero: '))
num2 = float(input('Informe um numero: '))
num3 = float(input('Informe um numero: '))

#menor numero
menor = num1

if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3

print('Menor número: ', menor)

#maior numero
maior = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

print('Maior número: ', maior)
