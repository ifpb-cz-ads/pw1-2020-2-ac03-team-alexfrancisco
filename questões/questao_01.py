velocidade = float(input('Qual a velocidade do carro agora ? '))
limite = 80

if velocidade > 80:
    valorMulta = ((limite - velocidade) * 5) * -1
    print('Você foi multado em R$ %f' %(valorMulta))