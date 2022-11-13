import random

print("Seja bem vindo ao jogo da advinhação")
numero = input("Digite o numero teto do desafio")

if numero.isdigit():
    numero = int(numero)
else:
    print("Erro!Valor inválido. Digite um numero")
    quit()

random_number = random.randint(0,numero)

n_chances = 0

while True:
    numero = input("Adivinhe o número: ")

    if numero.isdigit():
        numero = int(numero)
    else:
        print("Erro! Valor não é numerico.")
        continue

    n_chances = n_chances + 1
    if numero == random_number:
        print("Acertou")
        break
    elif numero > random_number:
        print("Chutou alto. O número é menor que isso")
    else:
        print("Chutou baixo. O número é maior que isso")

print("N° de tentativas" + str(n_chances))