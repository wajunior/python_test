from random import randint

continuar = True

while continuar:
    opt = str(input('Gostaria de jogar os dados (S / N): ')).lower().strip()
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    if 's' in opt:
            print('Valores dos dados!\n'
                  'Dado 1: {}\n'
                  'Dado 2: {}\n'
                  'Soma dos dados: {}'.format(dado1, dado2, dado1 + dado2))

    else:
        continuar = False
        print('Saindo do jogo!')
