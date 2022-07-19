frase = list(input('Informe uma frase com 10 caracteres: '))
for c in frase:
    if c in 'aeiou':
        frase.remove(c)
print()
print(f'A lista tem {len(frase)} consoantes\n'
      f'São elas: {frase}')
