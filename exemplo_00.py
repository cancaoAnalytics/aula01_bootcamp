nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
bonus_percentage = float(input("Percentual de bônus (de 0.0 a 100.0): "))

bonus = 1000 + (salario * (bonus_percentage/100))

print(f"{nome}, seu bônus é de {bonus:.2f}.")