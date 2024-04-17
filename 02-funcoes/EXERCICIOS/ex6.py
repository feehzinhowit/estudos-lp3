def converter(nota):
    if (nota <= 100 and nota >= 90):
        print('A nota é A')
    elif (nota <= 89 and nota >= 70):
        print('A nota é B')
    elif (nota <= 69 and nota >= 50):
        print('A nota é C')
    elif (nota <= 49 and nota >= 30):
        print('A nota é D')
    elif (nota <= 29 and nota >= 10):
        print('A nota é E')
    else:
        print('A nota é F')

nota = int(input('Digite a nota: '))
converter(nota)