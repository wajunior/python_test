salario = float(input('Informe seu salário: R$ '))
step = int(input('Informe quantos níveis subiu: '))
novosal = aumento = nivel = d = 0

if step == 1:
    nivel = salario * 5 / 100
    novosal = salario + nivel
else:
    for c in range(1, step):
        nivel = salario * 5 / 100
        aumento = salario + nivel
        d += aumento * 5 / 100
        novosal = d + aumento
print(f'Seu novo salário com o aumento de {step} níveis, será de R$ \033[32m{novosal:.2f}\033[m')
