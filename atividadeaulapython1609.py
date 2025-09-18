### x+=1
naopode = 0
pode = 0

import os; os.system('cls')
visitantes = int(input("Insira o número de visitantes: "))
alturamin = float(input("Insira a altura minima [EX: 1.50]: "))
alturamax = float(input("Insira a altura maxima [EX: 1.90]: "))

for i in range(1, visitantes + 1
               ):
    print(f"Visitante {i} insira sua altura:")
    altura = float(input())

    if altura >= alturamin and altura <= alturamax:
        print("Você pode ir ao brinquedo")
        pode = pode + 1
    else: 
        print("Voce nao pode ir ao brinquedo")
        naopode = naopode + 1

print(f"A quantidade de visitantes que poderão será {pode} e a quantidade que não {naopode}")
    
