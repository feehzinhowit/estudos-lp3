 def verificaPalindromo(palavra):
    palindromo = palavra[::-1]
    if palavra == palindromo:
        print('Sua palavra é um palindromo')
    else:
        print('Sua palavra não é um palindromo')
       
palavra = input('Digite uma palavra: ')
verificaPalindromo(palavra)