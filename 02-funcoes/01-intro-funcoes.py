# FUNCOES

# quero somar uma lista de numeros 
# usar a funcao sum()

# quero calcular medio de notas dos alunos 
# 1. tem no python?
# 2. alguem ja programou? 
# declarar


# DECLARACAO 
# def nome_funcao(parametro1, parametro2)
#   return valor


# CHAMADA 
# nome_funcao (parametro1, paramero2)
# print('ola')
# sum (1, 2, 3)


# EXEMPLOS DE FUNCOES

# funcao sem retorno e sem parametros
def imprimir_mensagem():
    print('socorroo')

imprimir_mensagem()
imprimir_mensagem()


# funcao sem retorno com paramentros 


# funcao com retorno e sem parametros 
def obter_mensagem():
    return 'socorroo'

mensagem = obter_mensagem()
print(mensagem)

print(obter_mensagem)


# funcao com retorno e com parametros
def gerar_saudacoes(nome):
    return f'bom dia {nome}'

print(gerar_saudacoes('pedro'))
print(gerar_saudacoes('ricardo'))

# imprimir saudacao 
def saudacoes(nome, frase):
    print(f'{frase} {nome}')

saudacoes('jonas', 'bom dia')

def saudacao(nome, frase):
    return f'{frase} {nome}'

print(saudacao('joao', 'bom dia'))


# entrada 
notas_alunos = [
    [10.0, 3.0, 3.0]
    [0.0, 1.0, 3.0]
    [9.0, 7.0, 3.0]
]

# saida [5.3, 1.3, 6.3]

def calcular_media(notas):
    return sum(notas) / len(notas)

def calcular_media_alunos(notas_alunos):
    medias = []

    for notas in notas_alunos: # nesse caso, o "notas" é cada linha da lista "notas_alunos"
        media = calcular_media(notas)
        medias.append(media)

    return medias
    # return [calcular_media(notas) for notas in notas_alunos]

