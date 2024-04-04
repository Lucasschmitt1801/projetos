lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))

if lado1 ** 2 + lado2 ** 2 == lado3 ** 2 or lado1 ** 2 + lado3 ** 2 == lado2 ** 2 or lado2 ** 2 + lado3 ** 2 == lado1 ** 2:
    print("O triângulo é retângulo.")
else:
    print("O triângulo não é retângulo.")