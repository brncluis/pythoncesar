import os;os.system('cls')
funcionarios = []
idades = []
funcionarios_validos = 0

qtd_funcionario = int(input("Informe a quantidade de funcionarios aptos a aposentadoria: "))

while funcionarios_validos < qtd_funcionario:
    nome = input("Insira a o nome do funcionario: \n")
    idade = int(input("Insira a idade do funcionario: \n"))
    if idade >= 60:
        funcionarios.append(nome)
        idades.append(idade)
        funcionarios_validos = funcionarios_validos + 1
    else:
        print("\nFuncionario não está apto a se aposentar.\n")

funcionario_mais_velho = max(idades)
indice_mais_velho = idades.index(funcionario_mais_velho)
media = sum(idades)/len(idades)

print("*"*35)
print("Funcionários a se aposentar em 2025")
for i in range(len(funcionarios)):
    print(f"Nome: {funcionarios[i]}    \t\tIdade: {idades[i]} anos")
print(f"Funcionario mais antigo: {funcionarios[indice_mais_velho]}")
print(f"Média de idades das aposentadorias: {media} anos")