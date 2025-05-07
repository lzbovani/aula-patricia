"""Escreva um algoritmo que pergunte o valor de uma mercadoria e qual o valor que o
usuário tem em mãos e diga se o dinheiro é ou não é suficiente para adquirir esta
mercadoria;"""

print('mercadoria')
mercadoria = float(input('qual o valor da mercadoria? '))
usuario = float(input('quanto você tem? '))

if usuario >= mercadoria:
    print('\nvoce consegue comprar o que voce quer')
    sobra = usuario - mercadoria
    print(f'e sobra {sobra}')

else:
    print('\nnão tem dinheiro para pagar')
