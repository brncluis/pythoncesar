import os;os.system('cls')
total = 0
while True:
    valor = float(input("Insira o valor do produto: "))

    if valor >= 1:
        total = total + valor
    elif valor == 0:
        break
    else: 
        print("Digite um valor positivo")

        
if total > 1000:
    total = total * 0.9
    print(f"Voce tem um desconto de 10% o total é {total}")
else: 
    print(f"O valor é {total}")

    