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




