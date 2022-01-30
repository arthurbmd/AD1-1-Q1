PI = 3.1415

while True:
    numero = input('Digite um número: ')

    if numero == '':        # Teste de variável vazia
        break
    
    numero = int(numero)

    if numero % 2 != 0:     # Teste de número ímpar
        area = PI * (numero ** 2)
        perimetro = 2 * PI * numero

        print(f'Área e Perímetro do Circulo de Raio {numero} são: {area:.2f} e {perimetro:.2f}')

    else:                   # Teste de número par
        print(f'Divisores de {numero} são: ', end='')
        for i in range(1,numero+1):
            if numero % i == 0:
                print(i, end=' ')
        print()