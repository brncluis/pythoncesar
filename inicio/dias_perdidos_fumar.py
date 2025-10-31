import os; os.system("cls")

mediadia = int(input("Quantos cigarros voce fuma por dia? "))
anos = float(input("Há quantos anos você fuma? "))

tempo = anos * 365 
perca = tempo * mediadia
percaminutos = float(perca * 10)
horas = float(percaminutos/60)
dia = float(horas/24)

print(f"O tempo perdido é {horas:.0f} horas e em dias é{dia: .2f}")
