
N = "ABCDFGKATUMKATMKAFKDNFDJNJNJGNJNRFVBHJBFJHSBHJDSBFHJBFJABIKNJKLENKATYJCNASDCKHJBVSKH"

P = "JABI"

j = 0

tam_n = len(N)
tam_p = len(P)
for i in range(tam_n):

    if j == tam_p-1 and N[i] == P[j]:
        print("Achou na palavra")
        break

    if N[i] != P[j]:
        j = 0
    else:
        j += 1


if j != tam_p-1:
    print("N achou")