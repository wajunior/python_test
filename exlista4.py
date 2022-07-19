from time import sleep

sistemasOp = votos = []
w = u = l = n = m = o = 0

print('Qual o melhor Sistema Operacional para uso em servidores?\n'
      'Escolha entre as opções abaixo')
print('-=' * 30)
print('[0] - Sair\n'
      '[1] - Windows server\n'
      '[2] - Unix\n'
      '[3] - Linux\n'
      '[4] - Netware\n'
      '[5] - Mac OS\n'
      '[6] - Outro')
print('-=' * 30)
while True:
    opc = int(input('Escolha uma opção: '))
    if 0 > opc > 6:
        print('Escolha inválida!')
    else:
        if opc == 0:
            print('Saindo do programa...')
            # sleep(1)
            break
        else:
            sistemasOp.append(opc)

for v in sistemasOp:
    if v == 1:
        w += 1
    elif v == 2:
        u += 1
    elif v == 3:
        l += 1
    elif v == 4:
        n += 1
    elif v == 5:
        m += 1
    else:
        o += 1
total = w + u + l + n + m + o

if total == 0:
    print('Não teve resultados')
else:
    print('-=' * 30)
    print(f'{"Sistema Operacional":<1}{"Votos":^20}{"%":>18}')
    print(f'{"-" * 19}{("-" * 5):^20}{("-" * 5):>20}')
    print(f'{"Windows Server":<1}{w:^30}{(w / total * 100):>15.2f}%')
    print(f'{"Unix":<1}{u:^50}{(u / total * 100):.2f}%')
    print(f'{"Linux":<1}{l:^48}{(l / total * 100):>6.2f}%')
    print(f'{"Netware":<1}{n:^43}{(n / total * 100):>9.2f}%')
    print(f'{"Mac OS":<1}{m:^45}{(m / total * 100):>8.2f}%')
    print(f'{"Outro":<1}{o:^48}{(o / total * 100):>6.2f}%')
    print(f'{"-" * 19}{("-" * 5):^20}')
    print(f'{"Total":<1}{total:^48}')
    print('-=' * 30)

    if w > u and w > l and w > n and w > m and w > o:
        print(f'O sistema operacional mais votado foi o Windows Server, com {w} votos, correspondendo a '
              f'{(w / total * 100):.2f}% dos votos.')
    elif u > w and u > l and u > n and u > m and u > o:
        print(f'O sistema operacional mais votado foi o Unix, com {u} votos, correspondendo a {(u / total * 100):.2f}%'
              f' dos votos.')
    elif l > w and l > u and l > n and l > m and l > o:
        print(f'O sistema operacional mais votado foi o Linux, com {l} votos, correspondendo a {(l / total * 100):.2f}%'
              f' dos votos.')
    elif n > w and n > u and n > l and n > m and n > o:
        print(f'O sistema operacional mais votado foi o Netware, com {n} votos, correspondendo a {(n / total * 100):.2f}%'
              f' dos votos.')
    elif m > w and m > u and m > l and m > n and m > o:
        print(f'O sistema operacional mais votado foi o Mac OS, com {m} votos, correspondendo a {(m / total * 100):.2f}%'
              f' dos votos.')
    else:
        print(f'O sistema operacional mais votado foi Outro, com {o} votos, correspondendo a {(o / total * 100):.2f}%'
              f' dos votos.')
