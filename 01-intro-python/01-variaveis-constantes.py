# identificadores 
# lerta, numero e _
# palavras reservadas (nao pode usar-las para criar variaveis): def, if, for...
# case sensitive: letra maiuscula importa

# o codigo termina com a identaçao

# VARIAVEIS
# identificador = valor
# altura = 1.8
# java: tipo identificador = valor (literal)
# tipagem dinamica: nao precisa escrev o tipo da variavel

altura = 1.8
idade = 22
nome = "Maria da Silva"
empregado = True

# CONSTANTES
# python nao tem constantes
pi = 3,14
PI = 3,14
# ambas podem mudar, porem, normalmente, variaveis com letra maisculas sao vistas como constantes

# COMENTARIOS
# uma linha 
"""
varias 
linhas 
"""

# DOCSTRING 
# documentacao de codigo de funcao
# classes, modulos, etc
def somar(n1, n2):
    """
    funçao que soma dois numeros
    
    :param n1: primeiro valor
    :param n2: segundo valor 
    :return: soma dos paramentros
    """
    return n1 + n2

somar (10, 2, 20.5)