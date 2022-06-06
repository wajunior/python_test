par = 0
impar = 0
for c in range(1, 6):
    num = int(input('Informe o {}º valor: '.format(c)))
    if num % 2 != 0:
        impar += 1
    else:
        par += 1

print('Total de numeros pares informado {}'.format(par))
print('Total de ímpares informados {}'.format(impar))
