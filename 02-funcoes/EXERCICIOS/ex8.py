 def contar(frase):
    dicionario = {}
    palavras = frase.split()
   
    for palavra in palavras:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
   
    return dicionario

frase = input('Digite uma frase: ')
resultado = contar(frase)
print(resultado)