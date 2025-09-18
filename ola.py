import os; os.system("cls")
distancia = float(input("Qual a distancia em KM: "))
velocidade = int(input("Qual a velocidade média do veiculo: "))
consumo = float(input("Qual o consumo médio do veiculo: "))
preco = float(input("Valor do combustivel/L: "))

tempo = distancia/velocidade
litros = distancia/consumo
total = litros * preco

print(f"O tempo estimado é de {tempo} horas\n")
print(f"O total de litros a ser gasto é {litros: .2f}\n")
print(f"O custo total estimado é de R${total: .2f}")