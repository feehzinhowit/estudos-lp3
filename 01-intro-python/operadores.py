# operadores aritmeticos
# +, -, *, /, **
nota1 = 10.0
nota2 = 5.5
nota3 = 7.5

media = (nota1 + nota2 + nota3) / 3


# numero elevado a outro
numero = 10
numero_elevado_2 = numero * numero
numero_elevado_2 = numero ** 2


# operadores logicos 
# and, or, not 
print(True and True) # True 
print(False and True) # False 
print(True and False) # False
print(False and False) # False

print(True or True) # True 
print(False or True) # True 
print(True or False) # True
print(False or False) # False

print(not True) # False
print(not False) # True


# permitir entrada 
# - o usuario for funcionario
# - o usuario nao estiver bloqueado 
# - hora atual estiver entre 8h e 18h

# permitir entrada 
# - admin

usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_admin = False

horario_comercial = hora_atual >= 8 and hora_atual <= 18
funcionario_ativo = usuario_funcionario and not usuario_bloqueado

if (funcionario_ativo and horario_comercial) or usuario_admin:
    print('acesso permitido')


# operadores de comparação
# ==, >=, <=, <, >, !=
# == --> comparando valores 
# = --> atribuindo o valor

idade = 25
maior_idade = idade >= 18 # true


# is, is not
# comparar se os objetos ocupam o mesmo espaco de memoria

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # true
print(a is b) # false

c = b
print(b is c) # true


# operador in, not in
# verificar se um elemento pertence a uma sequencia 

opcoes = ('sim', 'nao', 'talvez')
opcao = input('Digite uma opcao ')
opcao = opcao.lower() # caso o usuario dif=gite letra maiuscula, ele vai deixar minuscula
opcao = opcao.strip() # caso tenha espaco depois ou antes da respostas, ele vai tirar

if opcao in opcoes:
    print('ok')
else:
    print('nao tem essa opcao')

numeros = [1, 2, 3, 6]
for numero in numeros: 
    print(numero)