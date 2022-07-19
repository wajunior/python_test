maiorpeso = menorpeso = maioralt = menoralt = mediapeso = mediaaltura = cont = idmaalt = idmenalt = idmapeso = \
    idmepeso = 0

while True:
    cod = int(input('Informe o código do cliente (Digite 0 [zero] para sair): '))
    if cod == 0:
        break
    else:
        altura = float(input('Informe a altura do cliente: '))
        peso = float(input('Informe o peso do cliente: '))
        cont += 1

        mediaaltura += altura
        mediapeso += peso

        if cont == 1:
            maioralt = menoralt = altura
            maiorpeso = menorpeso = peso
            idmaalt = idmenalt = idmapeso = idmepeso = cod
        else:
            if altura > maioralt:
                maioralt = altura
                idmaalt = cod
            if altura < menoralt:
                menoralt = altura
                idmenalt = cod

            if peso > maiorpeso:
                maiorpeso = peso
                idmapeso = cod
            if peso < menorpeso:
                menorpeso = peso
                idmepeso = cod

print('-=' * 30)
print(f'Cliente mais alto:\n'
      f'Código: {idmaalt}\n'
      f'Altura: {maioralt:.2f}')
print('-=' * 30)
print(f'Cliente mais baixo:\n'
      f'Código: {idmenalt}\n'
      f'Altura: {menoralt:.2f}')
print('-=' * 30)
print(f'Cliente de maior peso:\n'
      f'Código: {idmapeso}\n'
      f'Peso: {maiorpeso:.2f}')
print('-=' * 30)
print(f'Cliente de menor peso:\n'
      f'Código: {idmepeso}\n'
      f'Peso: {menorpeso:.2f}')
print('-=' * 30)
print(f'Média de altura: {(mediaaltura / cont):.2f}\n'
      f'Média de peso: {(mediapeso / cont):.2f}')
