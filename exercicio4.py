n = int(input("digite um numero inteiro positivo:"  ))
divisor = 2
while n !=1:
    if n % divisor == 0:
        print(divisor)
        n = n/divisor
    else:
        divisor = divisor+1

