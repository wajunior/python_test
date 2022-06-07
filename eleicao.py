candidatoA = 0
candidatoB = 0
candidatoC = 0
cont = 1

print('=' * 50)
print('{:^50}'.format('Eleições 2022'))
print('=' * 50)

while cont != 0:
    op = str(input('Gostaria de iniciar as votações? [S/N]: ')).lower()

    if op == 's':
        c = 1

        while c != 0:
            eleitores = int(input('Informe a quantidade de eleitores: '))
            c += 1

            for n in range(1, eleitores + 1):
                print('======== ELEITOR Nº {} ========'.format(n))
                votos = int(input('[1] - Bolsonaro\n'
                                  '[2] - Lula\n'
                                  '[3] - Ciro Gomes\n'
                                  ': '))
                if votos == 1:
                    candidatoA += 1
                elif votos == 2:
                    candidatoB += 1
                elif votos == 3:
                    candidatoC += 1
                else:
                    print('Valor incorreto!')

            opc = str(input('Gostaria de continuar? [S/N]: ')).lower()

            if opc != 's':
                print('Saindo do programa!')
                c = 0
                cont = 0

    else:
        print('Saindo do programa!')
        cont = 0

print('-' * 50)
print('{:^50}'.format('Resultado da eleição!'))
print('-' * 50)

print('Bolsonaro = {}\n'
      'Lula = {}\n'
      'Ciro Gomes = {}'.format(candidatoA, candidatoB, candidatoC))
