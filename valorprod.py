v1 = float(input('Informe o valor do primeiro produto: R$ '))
v2 = float(input('Informe o valor do segundo produto: R$ '))
v3 = float(input('Informe o valor do terceiro produto: R$ '))

menor = v1

if v2 < v1 and v2 < v3:
    menor = v2
elif v3 < v1 and v3 < v2:
    menor = v3

print('Com base nos valores, o produto que vc deve comprar é com valor {}'.format(menor))