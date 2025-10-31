import os;os.system('cls')
vasc = int(input("Essa planta tem vascularização?\nSim[1]\nNão[2]\n"))
sementes = int(input("Essa planta tem sementes?\nSim[1]\nNão[2]\n"))
flores = int(input("Essa planta tem flores?\nSim[1]\nNão[2]\n"))

if flores == 0 and sementes == 0 and vasc == 0:
    print("A planta é briofita")
elif flores ==0 and sementes == 0 and vasc == 1:
    print("A planta é pteridofita")
elif flores ==0 and sementes == 1 and vasc == 1:
    print("A planta é giminiosperma")
elif flores == 1 and sementes == 1 and vasc == 1:
    print("A planta é angiosperma")
else: 
    print("Digite uma opção válida") 