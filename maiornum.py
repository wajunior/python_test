maior = 0
menor = 0
soma = 0

for c in range(1, 6):
    num = int(input('Informe o {}º valor: '.format(c)))

    if num < 0 or num > 1000:
        print('Informe um valor válido entre 0 e 1000')
        break
    else:
        if c == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
soma = maior + menor

print('O maior valor é {}\n'
      'O menor valor é {}\n'
      'A soma dos valores é {}'.format(maior, menor, soma))
