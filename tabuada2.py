tab = int(input('Informe qual tabuada gostaria de verificar: '))
com = int(input('Começando de qual número?: '))
ter = int(input('Terminando em qual número?: '))

if com < ter:
    print('Valor inicial menor que o final, favor digitar novamente!')
else:
    for c in range(com, ter+1):
        print(f'{tab:^2} x {c:^2} = {tab*c:^2}')
