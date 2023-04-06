a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Digite um terceiro número inteiro: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c: 
        print('Equilátero')
    else:
        if (a == b) or (b == c) or (c == a):
            print('Isósceles')
        elif (a != b) and (b != c) and (c != a):
            print('Escaleno')
else:
    print('Não é um triângulo')