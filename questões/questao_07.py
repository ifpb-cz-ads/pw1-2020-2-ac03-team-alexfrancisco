kwh = int(input('Informe a quantidade de kWh consumida: '))
instalacao = input('Qual o tipo de instalação ? (R, I, C) ')
valorAPagar = 0

if instalacao == 'R':

    if kwh <= 500:
       valorAPagar = (kwh * 0.4)
    else:
        valorAPagar = (kwh * 0.65)

elif instalacao == 'I':

    if kwh <= 5000:
       valorAPagar = (kwh * 0.55)
    else:
        valorAPagar = (kwh * 0.6)

elif instalacao == 'C':

    if kwh <= 1000:
       valorAPagar = (kwh * 0.55)
    else:
        valorAPagar = (kwh * 0.6)

else:
   print('Não reconhecemos esse tipo de instalação.')

print('O valor a ser pago é de R$ %f' %(valorAPagar))