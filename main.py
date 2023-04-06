a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Digite um terceiro número inteiro: '))

ab = b-a
bc = c-b
ca = a-c

if (a + b > c) and (a + c > b) and (b + c > a):
    if ab == bc == ca: 
        print('Equilátero')
    else:
        if (ab == bc) or (bc == ca) or (ca == ab):
            print('Isósceles')
        elif (ab != bc) and (bc != ca) and (ca != ab):
            print('Escaleno')
else:
    print('Não é um triângulo')