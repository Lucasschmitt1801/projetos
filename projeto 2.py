def ordenar_numeros(a, b, c):
    if a <= b:
        if b <= c:
            print(a, b, c)
        else:
            if a <= c:
                print(a, c, b)
            else:
                print(c, a, b)
    else:
        if a <= c:
            print(b, a, c)
        else:
            if b <= c:
                print(b, c, a)
            else:
                print(c, b, a)

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

print("Números em ordem crescente:")
ordenar_numeros(num1, num2, num3)


