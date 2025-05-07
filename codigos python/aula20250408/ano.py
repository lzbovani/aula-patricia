print("Escreva um ano que esta entre 1000 e 2999.")
ano = int(input("Digite um ano: "))
if ano < 1000 or ano > 2999:
  print("numero não esta entre 1000 e 2999")
elif(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")


