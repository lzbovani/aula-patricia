print('Caixa D agua')
bloco = int(input('qual bloco você mora? '))

if bloco % 2 == 0 and bloco <5 and bloco > 1:
    print('caixa A')

elif bloco % 2 != 0 and bloco <5 and bloco >= 1:


    print('caixa B')
else:
    print('bloco invalido')