import os; os.system("cls")
ncarros = int(input("Quantos carros você vendeu? "))
total_vendas = float(input("Qual faturamento de suas vendas? "))
salario = float(input("Seu sálario fixo? "))

comissao = total_vendas * 0.05 
comissaocarros = 1000 * ncarros
valor_total = comissao + comissaocarros + salario

print(f"O valor da sua comissão por faturamento é R${comissao}\n O valor da comissao por carro vendido é R${comissaocarros} \n E a soma de comissões e sálarios é R${valor_total}")




