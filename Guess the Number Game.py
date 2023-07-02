import random

dice = random.randint(1, 100)
#Uma varável que armazena o número que vai ser gerado.
while True:
#Um laço de repetição
    try:
    #Aqui a um tratamento de erro.
        number = int(input("Digite um numero aleatorio:"))
        #Uma pergunta para o usuário, onde ele tem que da um palpite sobre o número que foi gerado. 
        if (number > dice):
            print("Chute mais baixo!")
            #Caso o usuário digite um número maior que o que foi gerado mostrara essa mensagem.
        elif (number < dice):
            print("Chute mais alto")
            #Caso o usuário digite um número menor que o que foi gerado mostrara essa mensagem.
        elif (number == dice):
            print("Parábens! Você acertou.")
            break
            #Caso o usuário digite o valor certo mostrara essa mensagem e encerrara o programa.
    except ValueError:
    #Um tratamento de erro do tipo ValueError.
            print("O valor que você digitou não é válido!")
            continue
            #Caso o usuário digite um valor que não é válido o programa continuara até que ele acerte.
    res = input("Você quer continuar?")
    if (res == "Sim"):
        continue
    else:
        break
    #Esse bloco de código que vai perguntar para o usuário. Caso ele queira continuar digitar S, se ele digitar qual valor que não seja S encerrara.
