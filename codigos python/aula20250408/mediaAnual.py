print("media anula FIAP")
nota = float(input("qual foi a sua média final? "))
if nota >=6 and nota <=10:
    print("aprovado")
elif nota <6 and nota>=0:
    print("reprovado")
else:
    print("nota invalida")