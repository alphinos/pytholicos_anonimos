
PALAVRA = input()
CRIBE = input()

tam_p = len(PALAVRA)
tam_c = len(CRIBE)

cont = 0

for i in range(tam_p - tam_c + 1):
    for j in range(tam_c):
        if j+i < tam_p:
            if PALAVRA[j+i] == CRIBE[j]:
                cont += 1
                break

print(tam_p-tam_c+1-cont)

#lEONARDO GOAT