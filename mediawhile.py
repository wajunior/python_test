cont = 1
media = 0
soma = 0

while cont != 0:
    n = int(input('Informe a {}ª nota: '.format(cont)))
    opc = str(input('Gostaria de continuar? [S/N]: ')).lower()
    soma += n
    media += 1
    cont += 1

    if opc != 's':
        cont = 0

print('Total de notas informadas: {}'.format(media))
print('Média = {:.2f}'.format(soma / media))
