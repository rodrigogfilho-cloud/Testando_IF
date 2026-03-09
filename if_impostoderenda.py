salario = float(input("Digite seu salário:"))
if salario <= 2428.8:
    print ("ISENTO")
elif salario <= 2826.65:
    print(f"7,5% de imposto e {round(salario*0.075,2)} R$")
elif salario <= 3751.05:
    print(f"15% de imposto e {round(salario*0.15,2)} R$")
elif salario <= 4664.68:
    print(f"22,5% de imposto e {round(salario*0.225,2)} R$")
else:
    print(f"27,5% de imposto e {round(salario*0.275,2)} R$")
