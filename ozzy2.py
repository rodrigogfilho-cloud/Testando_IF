operacao = input("""
                 
                 Operações matemáticas:

+ SOMA 
- SUBTRAÇÃO
* MULTIPLICAÇÃO
/ DIVISÃO    
                 
                 Escolha uma das operações a cima:""")
numero1 = float(input("Digite o primeiro número da operação:"))
numero2 = float(input("Digite o segundo número da operação:"))

if operacao == '+':
            print(f"Resultado: {numero1 + numero2}")
elif operacao == '-':
            print(f"Resultado: {numero1 - numero2}")
elif operacao == '*':
            print(f"Resultado: {numero1 * numero2}")
elif operacao == '/':
             print(f"Resultado: {numero1 / numero2}")
            