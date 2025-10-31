#receber ano
#func 10 anos + ganha 30%
#func 5 a 10 anos  ganha 20¨%
# func menos 5 anos ganha 10%
# se recebeu ajuste ha menos de 2 anos nao ganha
# ano de admissao
#salario atual
#ano do ultimo reajuste
# mostrar novo salario ou impossibilidade de ajuste 
import os; os.system('cls')

slr = float(input("Informe seu sálario atual: "))
admissao = int(input("Informe seu ano de admissão: "))
reajuste = int(input("Informe o ultimo ano do seu reajuste: "))

tempo = 2025 - admissao

if reajuste < 2023:
    if tempo >=10:
        salario = slr * 1.30
        print(f"Seu novo sálario é {salario}")
    elif tempo >= 5 and tempo <= 10:
        salario = slr * 1.20
        print(f"Seu novo sálario é {salario}")
    elif tempo < 5:
        salario = slr * 1.10
        print(f"Seu novo sálario é {salario}")
else:
    print("Você já teve um reajuste recente")
