print("triangulo")


x1 = float(input("Digite o primeiro lado: "))
x2 = float(input("Digite o segundo lado: "))
x3 = float(input("Digite o terceiro lado: "))

if x1 + x2 > x3 and x1 + x3 > x2 and x2 + x3 > x1:
    if x1 == x2 == x3:
        print("Equilátero")
    elif x1 == x2 or x1 == x3 or x2 == x3:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("não é um triangulo")
