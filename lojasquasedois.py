print('#' * 50)
print('{:^50}'.format('TABELA DE PREÇOS'))
print('#' * 50)

p = 0

print('{:^2} | {:^2}'.format('Qtd', 'Valor'))
for c in range(1, 51):
    p += 1.99
    print('{:^2} = R$ {:.2f}'.format(c, p))
