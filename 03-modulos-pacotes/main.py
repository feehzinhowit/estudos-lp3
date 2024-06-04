# MODULOS

# importa todos os elementos de "matematica"
# tem que colocar o nome do modulo na frente de todos os elementos
import matematica

print(matematica.PI)
print(matematica.somar(10.0, 3.2))
print(matematica.subtrair(10.0, 3.2))


# importa so os elementos que voce quiser 
from matematica import PI, somar, subtrair
# from matematica import * (* = tudo)

print(matematica.PI)
print(matematica.somar(10.0, 3.2))
print(matematica.subtrair(10.0, 3.2))

# pra renomear os elementos
# LATORRE FALOU QUE É IMPORTANTE!!
from matematica import PI as PI_MAT


# importar a fn media do pacote estatisticas e modulo descritiva
from estatistica.descritiva import media