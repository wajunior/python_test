from random import randint
print('\nJogo da adivinhação, o computador está pensando em um numero de 1 a 10, tenta adivinhar!')

sorteio = randint(1, 10)
num = int(input('Informe um numero: '))
cont = 1

while sorteio != num:
    cont = cont + 1
    print('Que pena, você errou, tente novamente!')
    num = int(input('Informe um numero: '))
else:
    print('\nVoce acertou!\n'
          'numero informado {}\n'
          'numero sorteado {}'.format(num, sorteio))

print('\nVocê precisou de {} jogadas para acertar!'.format(cont))
