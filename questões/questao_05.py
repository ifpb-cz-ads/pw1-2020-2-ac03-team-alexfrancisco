n1 = float(input('Informe o primeiro número da operação: '))
n2 = float(input('Informe o segundo número da operação: '))
operacao = input('Informe qual operação deseja realizar: ')
resultado = eval('%f %s %f' %(n1, operacao, n2))

print('Resultado: %f' %resultado)