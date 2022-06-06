from random import choice
from time import sleep

print('\033[33m-=-\033[m' * 20)
print('\033[1;7;40m{:^60}\033[m'.format('JOKENPÔ'))
print('\033[33m-=-\033[m' * 20)

print('=' * 60)
print('Escolha entre:\n'
      'PEDRA - PAPEL - TEROUSA\n\n'
      'PEDRA ganha de TESOURA\n'
      'TESOURA ganha de PAPEL\n'
      'PAPEL ganha de PEDRA.')
print('=' * 60)

cont = True

while cont:
    comp = choice(['Pedra', 'Papel', 'Tesoura']).lower()
    opt = str(input('Gostaria de começar a jogar? (sim/não) ')).lower().strip()

    if opt == 'sim':

        player = str(input('Escolha sua opção: ')).lower()

        if player == 'pedra' or player == 'papel' or player == 'tesoura':
            print('\nO RESULTADO FOI...')
            print('=' * 60)

            sleep(2)

            if comp == player:
                print('Deu impate!')
                print('Computador escolheu: {}\n'
                      'Player escolheu: {}'.format(comp.upper(), player.upper()))

            elif comp == 'pedra' and player == 'tesoura':
                print('Computador Venceu!')
                print('Computador escolheu: {}\n'
                      'Player escolheu: {}'.format(comp.upper(), player.upper()))
            elif comp == 'tesoura' and player == 'papel':
                print('Computador Venceu!')
                print('Computador escolheu: {}\n'
                      'Player escolheu: {}'.format(comp.upper(), player.upper()))
            elif comp == 'papel' and player == 'pedra':
                print('Computador Venceu!')
                print('Computador escolheu: {}\n'
                      'Player escolheu: {}'.format(comp.upper(), player.upper()))

            if player == 'pedra' and comp == 'tesoura':
                print('Player Venceu!')
                print('Computador escolheu: {}\n'
                      'Player escolheu: {}'.format(comp.upper(), player.upper()))
            elif player == 'tesoura' and comp == 'papel':
                print('Player Venceu!')
                print('Computador escolheu: {}\n'
                      'Player escolheu: {}'.format(comp.upper(), player.upper()))
            elif player == 'papel' and comp == 'pedra':
                print('Player Venceu!')
                print('Computador escolheu: {}\n'
                      'Player escolheu: {}'.format(comp.upper(), player.upper()))

        else:
            print('Opção Inválida!')

    else:
        cont = False
        print('Saindo do Jogo!')
