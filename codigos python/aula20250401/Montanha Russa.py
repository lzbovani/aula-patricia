print('Montanha Russa')
titulo = 'Montanha Russa'
#algoritmo que calcula se a pessoa pode entrar na montanha russa
print(f'{titulo:^30}')

nome = input('Qual o seu nome?: ')
altura = float(input('Qual a sua altura?: '))

if altura >= 1.4:
    print('Voce pode ir na montanha russa')
    print(f'o usuario {nome} tem {altura} de altura')
else:
    print('Voce nao pode ir na montanha russa')
    print(f'o usuario {nome} tem {altura} de altura')
#print('o usuario ', nome,'tem',altura,'de altura')
#print(f'o usuario {nome} tem {altura} de altura')