import random

dice = random.randint(1, 100)
while True:
    number = int(input("Digite um numero aleatorio:"))
    if (number > dice):
        print("Chute mais baixo!")
    elif (number < dice):
        print("Chute mais alto")
    elif (number == dice):
        print("Parábens! Você acertou.")
        break
    else:
        print("O valor que você digitou não é válido!")
        continue
    res = input("Você quer continuar?")
    if (res == "Sim"):
        continue
    else:
        break