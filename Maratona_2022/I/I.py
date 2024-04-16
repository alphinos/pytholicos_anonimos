#Questão I

bits = list(map(int, input().split())) #Entrada contendo os Bits
erro = 0 #Flag para se não tiver erro
for i in bits:
    if i == 9: #Se tiver erro imprime 'F' e modifica a Flag
        print('F')
        erro = 1
        break

#Se não tiver erro imprime 'S'
if not(erro):
    print('S')