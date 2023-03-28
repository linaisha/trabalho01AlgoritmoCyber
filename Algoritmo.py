"""
01. Sistema de recomendação de livros:
Tipos de comida: Japonesa, Italiana, Mexicana, Brasileira, Chinesa
Valor do prato: Barato, Medio, Caro.
"""
cul = int(input("\n1. Japonesa\n2. Italiana\n3. Mexicana\n4. Brasileira\n5. Chinesa \n\nDigite o número correspondente a nacionalidade do prato:"))
val = int(input("\n1. Barato\n2. Médio \n3. Caro \n\nDigite o número correspondente ao valor:"))

if (cul == 1) and (val == 1): 
    print ("O restaurante sugerido é Sushi Yama")
elif (cul == 1) and (val == 2):
    print ("O restaurante sugerido é Kanpai")
elif (cul == 1) and (val == 3):
    print ("O restaurante sugerido é é Aizomê")
elif (cul == 2) and (val == 1):
    print ("O restaurante sugerido é Spaghetti Notte")
elif (cul == 2) and (val == 2):
    print ("O restaurante sugerido é Pizza Italiana")
elif (cul == 2) and (val == 3):
    print ("O restaurante sugerido é Fasano")
elif (cul == 3) and (val == 1):
    print ("O restaurante sugerido é La Mexicana")
elif (cul == 3) and (val == 2):
    print ("O restaurante sugerido é Si Senõr")
elif (cul == 3) and (val == 3):
    print ("O restaurante sugerido é Mexilhão")
elif (cul == 4) and (val == 1):
    print ("O restaurante sugerido é Churrascaria Vento")
elif (cul == 4) and (val == 2):
    print ("O restaurante sugerido é Fogo de Chão")
elif (cul == 4) and (val == 3):
    print ("O restaurante sugerido é Rubaiyat")
elif (cul == 5) and (val == 1):
    print ("O restaurante sugerido é China in Box")
elif (cul == 5) and (val == 2):
    print ("O restaurante sugerido é Ting Yuan")
elif (cul == 5) and (val == 3):
    print ("O restaurante sugerido é Mr. Lam")
else:
    print ("Erro, tente novamente")
    exit()