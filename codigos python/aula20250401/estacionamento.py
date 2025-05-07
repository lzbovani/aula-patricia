"""Um estacionamento cobra R$ 5,00 por hora porém possui um teto de cobrança
máxima de R$ 35,00, independente do número de horas. Escreva um algoritmo que
pergunte ao usuário qual foi o período de permanência em horas e escreva na tela o
total a pagar;"""
print('estacionamento')
hora = int(input('quantas horas voce ficou no estacionamento? '))

if hora < 7 and hora >= 1:
    pagar = hora * 5
    print('tem que pagar', pagar, 'reais')
else:
    print('tem que pagar 35 reias')