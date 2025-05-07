print('Sindico')

"""Um condomínio possui 20 blocos e para uma correta administração possui dois
síndicos: o sr José que administra os blocos de 1 a 10 e o sr Hamilton que administra
os blocos de 11 a 20. Escreva um algoritmo que pergunte ao usuário em qual bloco
ele mora e escreva na tela qual o síndico responsável;"""

bloco = int(input('qual o seu bloco? '))

if bloco >= 1 and bloco<=10:
    print('sr josé')
elif bloco >= 11 and bloco <=20:
    print('sr hamilton')
else:
    print('bloco invalido')
