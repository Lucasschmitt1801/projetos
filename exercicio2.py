n = int(input("digite um numero inteiro positivo:"  ))
divisores= 0
for divisor in range (1, n+1):
    if n % divisor == 0:
        divisores = divisores+1
    print(divisores)
