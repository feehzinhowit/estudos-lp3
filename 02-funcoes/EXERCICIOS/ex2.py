def tabuada(num):

    r = 1

    while(r <= 10):

        print(f'{num} * {r} = {num * r}')

       

        r = r + 1

       

num = int(input('Digite um numero entre 1 a 10: '))

tabuada(num)
