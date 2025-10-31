print("Escolas CESAR SCHOOL")
maior7 = 0
for i in range(1,6):
    nome = input("Insiria o nome da escola")
    print("Informe a média da escola")
    media = int(input())
    
    mediageral=+media

    if media >= 7:
        maior7 = maior7 + 1

print(f"Médias maiores que 7.0: {maior7}")
print(f"A soma das médias é: {mediageral}")



    
