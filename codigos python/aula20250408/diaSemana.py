print("DIA DA SEMANA")
dia = int(input("Entre com um numero de 1 a 7: "))

if dia == 1:
    print("domingo")
elif dia == 2:
    print("segunda")
elif dia == 3:
    print("terça")
elif dia == 4:
    print("quarta")
elif dia == 5:
    print("quinta")
elif dia == 6:
    print("sexta")
elif dia == 7:
    print("sabado")
else:

    print("numero invalido")

match dia:
    case 1 | 7:
        print("final de semana")
    case 2 | 3 | 4 | 5 | 6: #o pipe (|) é como se fosse o or 
        print("dia util")
    case _: #o _ é igual ao else do if
        print("dia invalido")