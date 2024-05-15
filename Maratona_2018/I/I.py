I, L = map(int, input().split())

lampadas = [0 for i in range(L)]

on_lamps = list(map(int, input().split()))

off_lamps = [0 for i in range(L)]

for i in range(1, on_lamps[0]+1):
    lampadas[on_lamps[i]-1] = 1

on_function = {}
lamps_states = { i: [] for i in range(1, I+1)}

for i in range(I):
    estados = list(map(int, input().split()))
    on_function[i+1] = estados[1:estados[0]+1]


def change_lamps(modify, lamps):
    tam_modify = len(modify)
    for i in range(tam_modify):
        index = modify[i]
        lamps[index-1] = (lamps[index-1]+1)%2


i = 1

contador = 1
impossible = False


change_lamps(on_function[i], lampadas)
lamps_states[i].append([l for l in lampadas])

i += 1

while lampadas != off_lamps:
    if i > I:
        i = i%I
    change_lamps(on_function[i], lampadas)
    if not(lampadas in lamps_states[i]):
        lamps_states[i].append([l for l in lampadas])
        contador += 1
    else:
        impossible = True
        break
    
    i += 1



if not impossible:
    print(contador)
else:
    print("-1")