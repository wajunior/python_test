n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
soma = 0

print('O valor informado foi {} e {}'.format(n1, n2))
print('Valores entre os numeros informado!')
for c in range(n1+1, n2):
    print('{}'.format(c), end=' ')
    soma += c
print('\nA soma dos valores do intervalo é igual a {}'.format(soma))
