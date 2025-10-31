import os; os.system('cls')
nutricao = { "suco de laranja" : 120, 
            "morango fresco" : 85, 
            "mamao" : 85, 
            "goiaba vermelha" : 70, 
            "manga" : 56, "laranja" : 50, 
            "brocolis" : 34,}

vitamina_frutas = []

def total_mg(vitamina_frutas):
    for i in range (len(vitamina_frutas)):
        if vitamina_frutas[i] > 109 and vitamina_frutas[i] < 131:
            print(f"{vitamina_frutas[i]} mg")

        elif vitamina_frutas[i] < 110:
            print(f"Mais {abs(vitamina_frutas[i] - 110)} mg")

        elif vitamina_frutas[i] > 130:
            print(f"Menos {abs(vitamina_frutas[i] - 130)} mg")
    

while True:
    qtd_mg = 0
    iteracoes = int(input())
    if iteracoes == 0:
        break
    else:
        for i in range (iteracoes):
            quantidade, fruta = input().split(" ", 1)
            quantidade = int(quantidade)
            if fruta in nutricao:           
                qtd_mg += quantidade * nutricao[fruta]
        vitamina_frutas.append(qtd_mg)

total_mg(vitamina_frutas)
