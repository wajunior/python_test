from random import choice

print('\033[1;34m-=-\033[m' * 20)
print('\033[1;31m{:^60}\033[m'.format('DADOS ERÓTICOS'))
print('\033[1;34m-=-\033[m' * 20)

cont = True
nome1 = str(input('Informe o nome do primeiro jogador: ')).upper().strip()
nome2 = str(input('Informe o nome do segundo jogador: ')).upper().strip()

while cont:
    jogar = str(input('Gostaria de rolar os dados? (S / N): ')).lower()
    dados1 = []
    dados2 = []

    print('\033[1;34m #\033[m' * 30)

    if 's' in jogar:
        print('Escolha o nível\n'
              '1 - Leve\n'
              '2 - Moderado\n'
              '3 - Pesado.')
        nivel = int(input('Escolha um nível: '))

        if nivel == 1 or nivel == 2 or nivel == 3:
            if nivel == 1:
                lista1 = ('beijar', 'acariciar', 'cheirar', 'assoprar', 'selinho', 'esfregar a boca')
                lista2 = ('boca', 'pescoço', 'orelhas', 'nuca', 'mãos', 'pés', 'pernas')
                dados1.extend(lista1)
                dados2.extend(lista2)

            elif nivel == 2:
                lista1 = ('massagear', 'beijar', 'beijar com vontade', 'lamber', 'apertar', 'dedilhar', 'acariciar',
                          'esfregar a bunda', 'esfregar o pau')
                lista2 = ('pescoço', 'nuca', 'peitos', 'pau', 'bolas', 'bunda', 'mamilos', 'virilha', 'buceta', 'boca',
                          'orelhas', 'pernas', 'rosto')
                dados1.extend(lista1)
                dados2.extend(lista2)

            elif nivel == 3:
                lista1 = (
                    'enfiar', 'meter com força', 'chupar', 'esfregar buceta', 'esfregar pau', 'lamber', 'estapear')
                lista2 = ('bunda', 'pau', 'buceta', 'bolas', 'cu', 'boca', 'peitos')
                dados1.extend(lista1)
                dados2.extend(lista2)

            print('\n{} deverá {} na/no {} do/a {}\n'.format(nome1, '\033[1;31m' + choice(dados1).upper(),
                                                             choice(dados2).upper() +
                                                             '\033[m', nome2))

        else:
            print('Opção inválida!')

    else:
        cont = False
        print('Obrigado por jogar')
