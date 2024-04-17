cand1 = 0
cand2 = 0
cand3 = 0

def votacao():
    global cand1, cand2, cand3
    i = 0
    
    print('+--------------------+')
    print('| 1. Maria           |')
    print('| 2. Joao            |')
    print('| 3. Latorre         |')
    print('+--------------------+')

    while (i <= 6):
        
        voto = int(input('Digite o numero do candidato que voce quer votar: '))
        
        if(voto == 1 or voto == 2 or voto == 3):
            if (voto == 1):
                cand1 = cand1 + 1
            elif (voto == 2):
                cand2 = cand2 + 1
            elif(voto == 3):
                cand3 = cand3 + 1
        else:
            print('Opcao invalida!')
            i = i - 1
        
        i = i + 1

    print('Votacao encerrada\n')

def analiseVencedor():
    print('Total de votos de cada participante')
    print(f'Maria: {cand1}')
    print(f'Joao: {cand2}')
    print(f'Latorre: {cand3}\n')
    
    if(cand1 > cand2 and cand1 > cand3):
        print('Maria ganhou a votacao')
    elif (cand2 > cand1 and cand2 > cand3):
        print('Joao ganhou a votacao')
    elif (cand3 > cand1 and cand3 > cand2):
        print('Latorre ganhou a votacao')
    else:
        print('Houve um empate e a votacao sera realizada novamente')
        votacao()
        analiseVencedor()
    

votacao()
analiseVencedor()