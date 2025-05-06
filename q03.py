n = 1
m = 1
z = 0

while n > 0 and m > 0:
    n = int(input('Insira o primeiro valor do par: '))
    m = int(input('Insira o segundo valor do par: '))
    if n or m > 0:
        if n > m and m > 0:
            while n > m:
                print(m)
                z = z + m
                m += 1
            if z > 0:
                print(f'A soma dos números é {z}')
        if n < m and n > 0:
            while m > n:
                print(n)
                z = z + m
                n += 1
            if z > 0:
                print(f'A soma dos números é {z}')


