n = int(input("digite um numero inteiro positivo:"  ))

for divisor in range (1, n+1):
    if n % divisor == 0:
        print(divisor)
