valor = float(input("Digite o valor da sua compra: "))

if(valor >= 0.01 and valor <= 9.99):
    desconto = 0.0
    valorDesconto = valor - (valor * desconto)
    print(valorDesconto)
    print(desconto * 100,"%")
elif(valor >= 10.0 and valor <= 99.99):
    desconto = 0.05
    valorDesconto = valor - (valor * desconto)
    print(valorDesconto)
    print(desconto * 100,"%")
elif(valor >= 100.0 and valor <= 499.99):
    desconto = 0.1
    valorDesconto = valor - (valor * desconto)
    print(valorDesconto)
    print(desconto * 100,"%")
elif(valor >= 500.0):
    desconto = 0.15
    valorDesconto = valor - (valor * desconto)
    print(valorDesconto)
    print(desconto * 100, "%")