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