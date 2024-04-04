jogador_a = input("Jogador A, o que você escolhe: pedra, papel ou tesoura? ")
jogador_b = input("Jogador B, agora é a sua vez: pedra, papel ou tesoura? ")

if jogador_a == jogador_b:
    print("Empate!")
elif jogador_a == "pedra":
    if jogador_b == "papel":
        print("Jogador B venceu!")
    else:
        print("Jogador A venceu!")
elif jogador_a == "papel":
    if jogador_b == "tesoura":
        print("Jogador B venceu!")
    else:
        print("Jogador A venceu!")
elif jogador_a == "tesoura":
    if jogador_b == "pedra":
        print("Jogador B venceu!")
    else:
        print("Jogador A venceu!")


