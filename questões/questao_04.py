
distancia = float(input('Informe a distância que deseja percorrer em KM:'))

if distancia <= 200:
    preco = distancia*0.5
    print('valor da passagem: R$%.2f' %preco)

else:
    preco = distancia*0.45
    print('valor da passagem: R$%.2f' %preco)
