# Setando variáveis
candidatoA = candidatoB = candidatoC = 0
cont = 1

print('=' * 50)
print('{:^50}'.format('Eleições 2022'))
print('=' * 50)

# Inicia as votações
while cont != 0:
    op = str(input('Gostaria de iniciar as votações? [S/N]: ')).lower()

    # Inicia as votações se a opção for S
    if op == 's':
        c = 1

        # Informa a quantidade de eleitores
        while c != 0:
            eleitores = int(input('Informe a quantidade de eleitores: '))
            c += 1

            # Começa o laço com a quantidade de eleitores informados
            for n in range(1, eleitores + 1):
                print('======== ELEITOR Nº {} ========'.format(n))
                votos = int(input('[1] - Bolsonaro\n'
                                  '[2] - Lula\n'
                                  '[3] - Ciro Gomes\n'
                                  ': '))

                # Computa quantos votos cada candidato teve
                if votos == 1:
                    candidatoA += 1
                elif votos == 2:
                    candidatoB += 1
                elif votos == 3:
                    candidatoC += 1
                else:
                    print('Valor incorreto!')

            # Pergunta se continua, para ou zera o resultado
            opc = str(input('Gostaria de continuar ou zerar resultados? [S/N/R(zerar)]: ')).lower()

            # Ação de sair do programa
            if opc == 'n':
                print('Saindo do programa!')
                c = 0
                cont = 0
            # Ação de zerar os votos informados anteriormente
            elif opc == 'r':
                votos = 0
                candidatoA = candidatoB = candidatoC = 0
    else:
        print('Saindo do programa!')
        cont = 0

print('-' * 50)
print('{:^50}'.format('Resultado da eleição!'))
print('-' * 50)

print('Bolsonaro = {}\n'
      'Lula = {}\n'
      'Ciro Gomes = {}'.format(candidatoA, candidatoB, candidatoC))
