lista = []
for c in range(0, 10):
    lista.append(float(input(f'Informe o {c}º valor: ')))
print('Sua lista de forma inversa: ', end='[')
for v in reversed(lista):
    print(v, end=', ')
print(']')
