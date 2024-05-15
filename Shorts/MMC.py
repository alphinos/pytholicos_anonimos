from time import perf_counter


#Algoritmo para Calcular o MMC entre dois numeros
def MMC_N2(A, B):

    factor = 2

    mmc = 1

    while A > 1 or B > 1:

        while A % factor == 0 or B % factor == 0:
            if A % factor == 0:
                A = A//factor
            if B % factor == 0:
                B = B//factor
            mmc *= factor

        factor += 1

        
    return mmc


#Algoritmo para Calcular o MMC entre mais de numeros. 
#Porém, bastava calcular o MMC de dois em dois, e depois pegar o mmc obtido como resultado e fazer com o numero seguinte.
def MMC_NN():
    factor = 2

    mmc = 1

    numbers = list(map(int, input().split()))
    tam_n = len(numbers)
    bases = [1 for i in range(tam_n)]

    begin = perf_counter()
    while numbers != bases:

        todos_dividem = True
        while todos_dividem:
            multi_rest = 1
            for i in range(tam_n):
               multi_rest *= numbers[i]%factor 
               if numbers[i]%factor == 0:
                   numbers[i] = numbers[i]//factor
            if multi_rest != 0:
                todos_dividem = False
            else:
                mmc *= factor
            
            
        factor += 1
    end = perf_counter()
    print(f"Tempo MMC_3 eh : {end - begin} segundos")
    return mmc
                  
#MMC de dois ou mais números usando apenas a função com dois. Em média 1,7 vezes mais rápido que MMC_NN()
def MMC_NN2():
   
    mmc = 1

    numbers = list(map(int, input().split()))
    tam_n = len(numbers)

    begin = perf_counter()
    for i in range(tam_n):
        mmc = MMC_N2(mmc, numbers[i])
    end = perf_counter()
    print(f"Tempo MMC_2_3 eh : {end - begin} segundos")
    return mmc





print(MMC_NN())
print(MMC_NN2())
#Usar como Teste
#10000 37461874564 16253261325 62352636









