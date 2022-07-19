print('=' * 30)
print(f'{"CÁLCULO DE GASTOS":^30}')
print('=' * 30)


salario = float(input('Informe seu salário: R$ '))
total = 0
porcentagem = salario * 30 / 100

while True:
    gastos = float(input('Informe o valor do gasto: R$ '))

    total += gastos

    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    while cont not in 'SN':
        print('Opção incorreta! ', end='')
        cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if cont == 'N':
        break

print('=' * 30)
print(f'Seu salário é: R$ {salario:.2f}\n'
      f'Seus gastos somam: R$ {total:.2f}')
print(f'30% do seu salário: R$ {porcentagem:.2f}\n'
      f'Gastos aceitável abaixo de R$ {salario - porcentagem:.2f}')


if total >= salario - porcentagem:
    print(f'Seus gastos superam seu orçamento de 30% do seu salário')
else:
    print(f'Seus gastos estão normalizados com seu orçamento de 30%')
