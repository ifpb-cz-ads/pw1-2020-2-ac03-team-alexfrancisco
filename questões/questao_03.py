salario = float(input('Informe o salário do funcionário: '))

if salario <= 1250:
    salario = salario + (salario * 0.15)
else:
    salario = salario + (salario * 0.10)

print('O novo valor corresponde à R$ %f' % (salario))