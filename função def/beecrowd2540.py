def verificar_imp(lista_votos):
    votos_pro = lista_votos.count("1")

    if votos_pro >= N * (2 / 3):
        return print("impeachment")
    else:
        return print("acusacao arquivada")
    
while True:
    try:
        lista_votos = []

        N = int(input())
        v = input().split()

        for votos in v:
            lista_votos.append(votos)

        verificar_imp(lista_votos)
    except EOFError:
        break