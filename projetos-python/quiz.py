print("Seja bem vindo ao nosso jogo")
user = input("Quer começar? [S/N]")

if user != "S":
    quit()

score = 0

print("Começando...")
print("Quem criou a Microsoft?\n(A)Bill Gates\n(B)Linus Torvalds\n(C)Steve Jobs")
user_1 = input("Resposta: ")

if user_1 == "A":
    print("Correto")
    score = score + 1
else:
    print("Incorreto")

print("Quem criou o Linux?\n(A)Bill Gates\n(B)Linus Torvalds\n(C)Steve Jobs")
user_2 = input("Resposta: ")

if user_2 == "B":
    print("Correto")
    score = score + 1
else:
    print("Incorreto")

print("Quem criou a Apple?\n(A)Bill Gates\n(B)Linus Torvalds\n(C)Steve Jobs")
user_3 = input("Resposta: ")

if user_3 == "C":
    print("Correto")
    score = score + 1
else:
    print("Incorreto")

print(f"Quiz acabou... Pontuação{score}/3")