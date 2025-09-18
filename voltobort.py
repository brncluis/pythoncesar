import os; os.system('cls')
level = int(input("Qual o nivel do voltorb: "))

if level >= 1 and level <=20:
    potencia = 20 + (level)**3
    print(f"A potencia do choque foi {potencia}W")
elif level >= 21 and level <=40:
    potencia = 8000 + (level - 10)**2
    print(f"A potencia do choque foi {potencia}W")
elif level >= 41 and level <= 60:
    potencia = 9000 + (5 * level)
    print(f"A potencia do choque foi {potencia}W")
elif level >= 61 and level <= 80:
    potencia = 9300 + (2 * level)
    print (f"A potencia do choque foi {potencia}W")
elif level >= 81 and level <= 100:
    potencia = 9500 + level
    print(f"A potencia do choque foi {potencia}W")
else:
    print("Digite um valor entre 1 e 100.")

