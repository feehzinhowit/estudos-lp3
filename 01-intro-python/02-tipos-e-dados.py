# TIPOS DE DADOS
# int, float
# string, list, tuple, set
# dict
# none 

# INT
idade = 28
temperatura = -30

# FLOAT 
altura = 1.55
PI = 3.14

#STRING 
nome = 'Felipe Witkowsky'
nome = "Felipe Witkowsky"
"""
para exibir o caracter da palavra 
print(nome[0]) ---> exibiria o F
print(nome[-1]) ---> como é negativo, pega de traz pra frente, exibiria o Y
"""

#CHAR (???)
letra = 'a'
letra ="a"

# nome eh um objeto da classe str
# nome tem seus metodos
print(nome.capitalize())
print(nome)

# INTERPOLACAO DE STRINGS E VARIAVEIS
# f-string 
nome = "joao"
idade = 22
mensagem = f"ola (nome), voce (idade) anos"
print(mensagem)

# LIST
# lista de valores 
# pode ser alterada

habilidades = []
habilidades = ['java', 'c#', 'css']
print(habilidades[0])
print(habilidades[-1])

habilidades[0] = 'javascript'

habilidades.append('html') # javascript, c#, css, html
habilidades.insert(0, 'kotlin') # kotlin, javascript, c#, css, html

# TUPLE 
# 'lista de valores'
# nao pode alterar (adicionar ou remover), eh tipo uma 'lista constante'
opcoes = ('sim', 'nao', 'talvez')

#SET 
# nao indexado
# nao permite elementos duplicados
emails = {'mariazinha@gmail.com', 'joaozinho@gmail.com', 'mariazinha@gmail.com'}
emails.add('mariazinha@gmail.com')
print(emails) # so vai exibir 1 vez o email da mariazinha


# DICT
# dicionario
# chave : valor 
# key : value 

# site de emprego 
empresa = 'Google'
titulo = 'Engenheiro de Software'
salario = 20000.00
remoto = False

# vaga 
vaga = {
    'empresa': 'Google',
    'titulo': 'Engenheiro de Software',
    'salario': 20000.00,
    'remoto': False
}

print(vaga['salario'])

# NONE 
nome = None