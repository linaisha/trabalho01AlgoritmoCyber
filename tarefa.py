"""
01. Sistema de recomendação de livros:

Gêneros: romance, ficção científica, fantasia, biografia, história, thriller.
Formatos: físico ou digital.
Exemplos de livros:
Romance: "Orgulho e Preconceito", de Jane Austen.
Ficção científica: "Neuromancer", de William Gibson.
Fantasia: "O Senhor dos Anéis", de J.R.R. Tolkien.
Biografia: "Steve Jobs", de Walter Isaacson.
História: "Sapiens", de Yuval Noah Harari.
Thriller: "O Código Da Vinci", de Dan Brown.
"""
"""
genero = int(input("Digite o número correspondente ao gênero do filme que gostaria de assistir:\n1. Romance\n2. Ficção "
               "científica\n3. Fantasia\n4. Biografia\n5. História\n6. Thriller \n"))
formato = int(input("Digite o número correspondente ao formato:\n1. Físico\n2. Digital \n"))
if (genero == 1) and (formato == 1):
    print("Alugue \"Orgulho e Preconceito\", de Jane Austen. Disponível na versão fisica.")
elif (genero == 1) and (formato == 2):
    print("Alugue \"Orgulho e Preconceito\", de Jane Austen. Disponível na versão digital.")
elif (genero == 2) and (formato == 1):
    print("Alugue \"Neuromancer\", de William Gibson. Disponível na versão fisica.")
elif (genero == 2) and (formato == 2):
    print("Alugue \"Neuromancer\", de William Gibson. Disponível na versão digital.")
elif (genero == 3) and (formato == 1):
    print("Alugue \"O Senhor dos Anéis\", de J.R.R. Tolkien. Disponível na versão fisica.")
elif (genero == 3) and (formato == 2):
    print("Alugue \"O Senhor dos Anéis\", de J.R.R. Tolkien. Disponível na versão digital.")
elif (genero == 4) and (formato == 1):
    print("Alugue \"Steve Jobs\", de Walter Isaacson. Disponível na versão fisica.")
elif (genero == 4) and (formato == 2):
    print("Alugue \"Steve Jobs\", de Walter Isaacson. Disponível na versão digital.")
elif (genero == 5) and (formato == 1):
    print("Alugue \"Sapiens\", de Yuval Noah Harari. Disponível na versão fisica.")
elif (genero == 5) and (formato == 2):
    print("Alugue \"Sapiens\", de Yuval Noah Harari. Disponível na versão digital.")
elif (genero == 6) and (formato == 1):
    print("Alugue \"O Código Da Vinci\", de Dan Brown. Disponível na versão fisica.")
elif (genero == 6) and (formato == 2):
    print("Alugue \"O Código Da Vinci\", de Dan Brown. Disponível na versão digital.")
else:
    print("Essa opção é inválida, recomece o programa.")
    exit()
"""
"""
02. Sistema de recomendação de filmes:

Gêneros: comédia, drama, ação, ficção científica, terror, romance.
Classificação indicativa: Livre, 10 anos, 12 anos, 14 anos, 16 anos ou 18 anos.
Exemplos de filmes:
Comédia: "Debi e Loide", dos irmãos Farrelly.
Drama: "Forrest Gump", de Robert Zemeckis.
Ação: "Duro de Matar", de John McTiernan.
Ficção científica: "Blade Runner", de Ridley Scott.
Terror: "O Iluminado", de Stanley Kubrick.
Romance: "Simplesmente Acontece", de Christian Ditter.
"""
"""
ano = int(input("Ano em que você nasceu: "))
idade = 2023 - ano

if idade < 10:
    genero = int(input("Digite o número correspondente ao gênero do filme que gostaria de assistir:\n1. Comédia\n2. "
                       "Drama"))
    if genero == 1:
        print("Você pode assistir:\nMinha mãe é uma peça\nShrek")
    elif genero == 2:
        print("Você pode assistir:\nMeu primeiro amor")
    else:
        print("Opção indisponivel.")
        exit()
elif idade < 12:
    genero = int(input("Digite o número correspondente ao gênero do filme que gostaria de assistir:\n1. Comédia\n2. "
                       "Drama\n3. Ação"))
    if genero == 1:
        print("Você pode assistir:\nShrek 2")
    elif genero == 2:
        print("Você pode assistir:\nMenino do pijama listrado")
    elif genero == 3:
        print("Você pode assistir:\nDuro de matar")
    else:
        print("Opção indisponivel.")
        exit()
elif idade < 14:
    genero = int(input("Digite o número correspondente ao gênero do filme que gostaria de assistir:\n1. Comédia\n2. "
                       "Drama\n3. Ação\n4. Ficção Científica"))
    if genero == 1:
        print("Você pode assistir:\nShrek 3")
    elif genero == 2:
        print("Você pode assistir:\nJogo do Coritiba")
    elif genero == 3:
        print("Você pode assistir:\nHitman")
    elif genero == 4:
        print("Você pode assistir:\nStar Wars")
    else:
        print("Opção indisponivel.")
        exit()
elif idade < 16:
    genero = int(input("Digite o número correspondente ao gênero do filme que gostaria de assistir:\n1. Comédia\n2. "
                       "Drama\n3. Ação\n4. Ficção Científica\n5. Terror"))
    if genero == 1:
        print("Você pode assistir:\nShrek 4")
    elif genero == 2:
        print("Você pode assistir:\nA culpa é das estrelas")
    elif genero == 3:
        print("Você pode assistir:\nVelozes e Furiosos")
    elif genero == 4:
        print("Você pode assistir:\nStar Trek")
    elif genero == 5:
        print("Você pode assistir:\nAlien")
    else:
        print("Opção indisponivel.")
        exit()
elif idade < 18:
    genero = int(input("Digite o número correspondente ao gênero do filme que gostaria de assistir:\n1. Comédia\n2. "
                       "Drama\n3. Ação\n4. Ficção Científica\n5. Terror\n6. Romance"))
    if genero == 1:
        print("Você pode assistir:\nShrek 5")
    elif genero == 2:
        print("Você pode assistir:\nLembranças")
    elif genero == 3:
        print("Você pode assistir:\nVelozes e Furiosos 2")
    elif genero == 4:
        print("Você pode assistir:\nStar Trek 2")
    elif genero == 5:
        print("Você pode assistir:\nA Coisa")
    elif genero == 6:
        print("Você pode assistir:\nBarraca do beijo")
    else:
        print("Opção indisponivel.")
        exit()
else:
    genero = int(input("Digite o número correspondente ao gênero do filme que gostaria de assistir:\n1. Comédia\n2. "
                       "Drama\n3. Ação\n4. Ficção Científica\n5. Terror\n6. Romance"))
    if genero == 1:
        print("Você pode assistir:\nShrek 6")
    elif genero == 2:
        print("Você pode assistir:\nMarley e eu")
    elif genero == 3:
        print("Você pode assistir:\nVelozes e Furiosos: Desafio em Tokio")
    elif genero == 4:
        print("Você pode assistir:\nInterstelar")
    elif genero == 5:
        print("Você pode assistir:\nA casa de cera")
    elif genero == 6:
        print("Você pode assistir:\nA última musica")
    else:
        print("Opção indisponivel.")
        exit()
"""
"""
03. Sistema de recomendação de restaurantes:
Tipos de comida: Japonesa, Italiana, Mexicana, Brasileira, Chinesa
Valor do prato: Barato, Medio, Caro.
"""
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
"""
"""
04. Sistema de recomendação de refeições:

1Restaurante Verde Vida:

Opções veganas: sim.
Ambiente: casual e acolhedor.
Faixa de preço: médio.
Pratos recomendados: salada de quinoa com legumes grelhados, hambúrguer vegano com batatas fritas, pudim de chia com frutas vermelhas.

2Restaurante Carne de Sol:

Opções veganas: não.
Ambiente: rústico e descontraído.
Faixa de preço: baixo-médio.
Pratos recomendados: carne de sol com macaxeira, arroz de camarão, feijão verde com torresmo.

3Restaurante Sabor Japonês:

Opções veganas: sim.
Ambiente: moderno e elegante.
Faixa de preço: médio-alto.
Pratos recomendados: sushi vegano, tempurá de legumes, yakissoba de frutos do mar.

4Restaurante La Bella Italia:

Opções veganas: sim.
Ambiente: sofisticado e acolhedor.
Faixa de preço: alto.
Pratos recomendados: lasanha de berinjela, penne ao molho de tomate e manjericão, torta de limão sem glúten.
Perguntas que você pode usar para criar um sistema de recomendação com base em preferências pessoais:

Qual é o seu orçamento?
Você prefere opções veganas ou não veganas?
Qual tipo de ambiente você prefere?
Qual é o seu prato favorito ou que você gostaria de experimentar?
Você tem alguma restrição alimentar, como glúten ou lactose?
Neste caso, crie um sistema que a pessoa escolhe de 1 a 3 perguntas, ou seja, não precisa responder todas.
"""
orc = int(input("Qual é seu orçamento:\n1. médio\n2. baixo-médio\n3. médio-alto\n4. alto "))
veg = int(input("Opção vegana ou não:\n1. Sim\n2. Não\n"))
amb = int(input("Tipo de ambiente preferivel:\n1. Casual e acolhedor\n2. Rústico e descontraido\n3. Moderno e "
                "elegante\n4. Sofisticado e acolhedor\n"))
prato = int("Qual seu prato favorito ou que gostaria de experimentar:\n1. salada de quinoa com legumes grelhados, "
            "hambúrguer vegano com batatas fritas, pudim de chia com frutas vermelhas\n2. carne de sol com macaxeira, "
            "arroz de camarão, feijão verde com torresmo\n3. sushi vegano, tempurá de legumes, yakissoba de frutos do "
            "mar\n4. lasanha de berinjela, penne ao molho de tomate e manjericão, torta de limão sem glúten")
restricao = int(input("Você possui restrição alimentar:\n1. Não\n2. Glúten\n3. Lactose"))

ponto1 = 0
ponto2 = 0
ponto3 = 0
ponto4 = 0

if orc == 1:
    ponto1 += 1
elif orc == 2:
    ponto2 += 1
elif orc == 3:
    ponto3 += 1
elif orc == 4:
    ponto4 += 1
else:
    print("Opção indisponivel.")
