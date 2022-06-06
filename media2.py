nota1 = float(input('Digite 1ª nota: '))
nota2 = float(input('Digite 2ª nota: '))
media = (nota1 + nota2) / 2

if media <= 4:
    print('Nota: {:.2f}\n'
          'Nota: E\n'
          'Reprovado!'.format(media))
elif 4 < media <= 6:
    print('Nota: {:.2f}\n'
          'Nota: D\n'
          'Reprovado!'.format(media))
elif 6 < media <= 7.5:
    print('Nota: {:.2f}\n'
          'Nota: C\n'
          'Aprovado!'.format(media))
elif 7.5 < media <= 9:
    print('Nota: {:.2f}\n'
          'Nota: B\n'
          'Aprovado!'.format(media))
else:
    print('Nota: {:.2f}\n'
          'Nota: A\n'
          'Aprovado!'.format(media))