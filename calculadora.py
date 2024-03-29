# Funções para operações matemáticas

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero!"
    else:
        return x / y

# Menu da calculadora

def menu():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

# Loop principal do programa

while True:
    menu()

    escolha = input("Digite a opção (1/2/3/4/5): ")

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado:", soma(num1, num2))

        elif escolha == '2':
            print("Resultado:", subtracao(num1, num2))

        elif escolha == '3':
            print("Resultado:", multiplicacao(num1, num2))

        elif escolha == '4':
            print("Resultado:", divisao(num1, num2))

    elif escolha == '5':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")
