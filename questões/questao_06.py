
valorCasa = float(input('Informe o valor da casa: '))
salário = float(input('Informe o seu salário:'))
prestacoes = int(input('Informe a quantidade de prestações:'))

valorPrestacao = valorCasa/prestacoes

percentual = salário*0.3

if valorPrestacao > percentual:
    print('Empréstimo Negado')
else:
    print('Solicitação aprovada, parcelas mensais de: R$%.2f' %valorPrestacao)

