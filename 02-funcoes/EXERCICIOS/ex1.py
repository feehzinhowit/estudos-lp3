import random

 

def advinhar():

    numero = random.randint(1, 100)

    while True:

        try:

            chute = int(input('Digite um numero: '))

            if chute == numero:

                print('Acertou')

                break

            elif chute > numero:

                print('Tente um numero mais baixo')

            elif chute < numero:

                print('Tente um numero mais alto')    

        except ValueError:

                print('Erro!')

advinhar()
