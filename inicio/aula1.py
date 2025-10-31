import os; os.system("cls")

nome = input("Qual seu nome:")
pedido = int(input("Qual número do pedido?"))
valor = float(input("Qual valor da compra?"))
tipopag = input("Como você deseja pagar:")

print(f"O cliente {nome} realizou o pedido {pedido} no valor de R${valor} e o seu pagamento será com {tipopag}")
