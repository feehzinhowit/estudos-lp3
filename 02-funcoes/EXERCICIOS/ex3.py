i = 0
j = 0

 
def letras(frase):

    global i

    global j

    for letra in fraseSemEspaco:

        letra = letra.capitalize()

        if(letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'):

            i = i + 1

        else:

            j = j + 1

           

frase = input('Digite uma frase: ')
fraseSemEspaco = frase.strip()

letras(fraseSemEspaco)

 

print(f'Sua frase tinha {i} vogais')

print(f'Sua frase tinha {j} consoantes')