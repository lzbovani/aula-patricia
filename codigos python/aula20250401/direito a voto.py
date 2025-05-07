print('direito a voto')
idade = int(input('sua idade: '))
nome = input('seu nome: ')

if idade >=16:
    print(f'{nome} pode votar ja que tem {idade} anos')
else:
    print(f'{nome} não pode votar ja que tem {idade} anos')