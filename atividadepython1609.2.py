### soma = soma + valor
## soma += valor
### deve ser inicializado com 0
soma = 0
numero = int(input("Insira o número: "))
for i in range(1, numero):
    if numero % i == 0:
        soma = soma + i

if soma == numero:
    print("O número é perfeito.")
else: 
    print("O número não é perfeito")

