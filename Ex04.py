distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prstes a começar um viagem de {}Km.'.format(distancia))
if distancia<= 200:
    preco = distancia * 0.50
    print('E o preço da sua passagem será de {}'.format(preco))
else:
    preco2 = distancia *0.45
    print('E o preço da sua passagem será de {}'.format(preco2))
