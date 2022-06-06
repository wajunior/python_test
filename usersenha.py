c = True

while c:
    user = input('Informe o usuário: ')
    pwd = input('Informe a senha: ')

    if user == pwd:
        print('Senha não pode ser igual ao usuário, Informe novamente!')
    else:
        print('usuário: {}'.format(user))
        print('senha: {}'.format(pwd))
        c = False
