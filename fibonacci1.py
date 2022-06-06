ultimo = 1
penul = 1
c = 0
termo = 0
num = int(input('Informe o valor de N de fibonacci: '))

print('A sequência até o {}º termo é'.format(num))

#if num == 1 or num == 2:
print('0 1 1', end=' ')
#else:
while c <= num:
    termo = ultimo + penul
    penul = ultimo
    ultimo = termo
    c +=1
    print('{}'.format(termo), end=' ')
