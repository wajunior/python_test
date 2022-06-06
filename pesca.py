peso = float(input('Digite o peso de peixe: '))
exe = peso - 50
multa = exe * 4

if peso <= 50:
    print('Peso {} dentro do limite padrão!'.format(peso))
else:
    print('Você excedeu em {:.2f}Kg o peso.\n'
          'Precisará pagar uma mulda de R$ {:.2f}'.format(exe, multa))
