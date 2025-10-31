ingresso = 40

idade = int(input("Digite sua idade: "))
estudante = input("Digite S se voce for estudante: ")
horario = int(input("Digite a hora da compra: "))

if estudante == "S":
    ingresso = ingresso * 0.5
elif idade >= 60:
    ingresso = ingresso * 0.80
elif horario >= 6 and horario <= 12:
    ingresso = ingresso * 0.8
else:
    print("Opção indisponivel")

print(f"Novo valor {ingresso}")