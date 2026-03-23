idade = int(input("Você tem +18 anos ? "))
autorização = input("Você tem autorização dos seus pais para assistir PANICO 7 ? ").upper() # ou "capitalize()"-> esse transforma todas as primeiras letras em maíusculo ou "lower()"->transforma todas as letras em minusculo ou "upper()"-> transforma todas as letras em maiúsculo
if idade > 18 or autorização == "SIM" or autorização == "S":
    print ("Você está autorizado para assistir ao filme")
else: 
    print("Sinto muuito, mas você não tem a idade devida idade nem autorização para entrar.")
