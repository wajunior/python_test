p = float(input('Informe o preço do pão: R$ '))
n = p

print('#' * 50)
print('{:^50}'.format('TABELA DE PREÇOS'))
print('#' * 50)

print('{:^2} | {:^2}'.format('Qtd', 'Preço'))
print('{:^2} = R$ {:.2f}'.format(1, p))
for c in range(2, 51):
    p += n

    print('{:^2} = R$ {:.2f}'.format(c, p))
