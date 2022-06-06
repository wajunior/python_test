from time import sleep

print('-=-' * 10)
print('JOGO DE DETETIVE!')
print('-=-' * 10)

print('-' * 100)
print('A vítima do sexo maculino de 36 anos foi encontrada inconciente com um ferimento de bala no peito.\n'
      'Responta as questões abaixo para determinar se você é Inocente, Suspeito, Cúmplice ou Assassino!')
print('-' * 100)

print('[1] - SIM\n'
      '[0] - NÃO')
a = int(input('Telefonou para a vítima? '))
b = int(input('Esteve no local do crime? '))
c = int(input('Mora próximo da vítima? '))
d = int(input('Devia para a vítima? '))
e = int(input('Já trabalhou com a vítima? '))

qtd = a + b + c + d + e

print('=' * 30)
print('VOCÊ FOI DECLARADO...')
print('=' * 30)

sleep(3)

if qtd < 2:
    print('INOCENTE!')
elif 0 < qtd <= 2:
    print('SUSPEITO!')
elif 2 < qtd <= 4:
    print('CÚMPLICE!')
else:
    print('ASSASSINO!')
