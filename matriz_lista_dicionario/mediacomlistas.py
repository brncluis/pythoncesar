import os; os.system('cls')

pesos_produtos = []

for i in range(2):
    produto = float(input("Insira o peso dos produtos: "))
    pesos_produtos.append(produto)

soma_pesos = sum(pesos_produtos)

print(f"O peso médio das vendas é {soma_pesos / len(pesos_produtos)}")
print(f"O menor peso vendido foi {min(pesos_produtos)}")
print(f"O maior peso vendido foi {max(pesos_produtos)}")
faturamento =  soma_pesos * 4.35 
print(f"{faturamento:.2f}")

