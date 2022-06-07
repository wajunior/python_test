turmas = int(input('Informe a quantidade de turmas: '))
qtd = 0
media = 0

for c in range(1, turmas+1):
    alunos = int(input('Informe a quantidade de alunos da turma {}: '.format(c)))

    if alunos > 40:
        print('Turma {} excedeu o límite de 40 alunos'.format(c))
    else:
        qtd += alunos
        media += 1

print('As {} turmas tem em média {:.1f} alunos'.format(turmas, qtd / media))
