'''
Árvore de Segmentação:
    Árvore construída com a ideia de armazenar realizar um determinado trabalho de tempo O(log n) em um vetor de N elementos.
    Como exemplo clássico, calcular a soma entre o i-ésimo e o j-ésimo elementos de um vetor.
    V = [1,2,3,4,5,6,,7,8,9,10]
    Calcular Soma_Em_V(3, 8) -> Soma entre os indices 3 e 8, incluindo eles:
        Da pra calcular em O(n) -> Basta percorrer o intervalo e somar tudo
        Mas em alguns problemas esse tempo pra percorrer o intervalo não é suficente para resolver o problema e temos TLE (Time Limit Exceed)
        Para resolver, podemos construir uma árvore de Segmentação
    
    Construção da Árvore:

    As folhas da Árvore serão os elementos do vetor. Seus pais receberão, nesse caso, a soma dos dois filhos
'''

V = list(map(int, input().split()))
S = [0 for i in range(4*len(V))]

#Build

def freq(l, r):
    if l[1] & r[1]:
        return (l[0]+r[0], l[1] & r[1])
    
    if l[0] == r[0]:
        return (l[0], l[1] | r[1])
    
    return l if l[0] > r[0] else r
    

def build(p: int, l: int, r: int):

    if l == r:
        S[p] = (1, set([V[l]]))
        return S[p]
    
    m = (l+r)//2
    
    freq_set = freq(build(2*p, l, m), build(2*p+1, m+1, r))

    if p == 1:
        S[p] = (freq_set[0], max(freq_set[1]))
    else:
        S[p] = freq_set

    return S[p]

build(1, 0, len(V)-1)
lazy = [0 for i in range(4*len(V))]
print(S)

def query(a: int, b:int, p:int, l:int, r:int):
    # print(S)
    if lazy[p] != 0:
        S[p] = ( S[p][0], {valor + lazy[p] for valor in S[p][1]})
        lazy[p] = 0

    if b < l or a > r:
        return (0, set())
    
    if a <= l and r <= b:
        return S[p]
    
    m = (l+r)//2
    # print(m)
    freq_set = freq(query(a, b, 2*p, l, m), query(a, b, 2*p+1, m+1, r))

    if p == 1:
        return (freq_set[0], max(freq_set[1]))
    else:
        return freq_set

    



def update(a: int, b:int,  v: int, p: int, l: int, r: int):

    if lazy[p] != 0:
        S[p] = ( S[p][0], {valor + lazy[p] for valor in S[p][1]})
        lazy[p] = 0

    if a > r or b < l:
        return S[p]
    
    if l >= a and r <= b:
        S[p] = ( S[p][0], {valor + v for valor in S[p][1]})
        lazy[2*p] += v
        lazy[2*p+1] += v
        return S[p]
    
    m = (l+r)//2

    freq_set =  freq(update(a, b, v, 2*p, l, m), update(a, b, v, 2*p+1, m+1, r))

    if p == 1:
        S[p] = (freq_set[0], max(freq_set[1]))
    else:
        S[p] = freq_set

    return S[p]


frequencia = query(0, 2, 1, 0, len(V)-1)[1]
print(S)
print(frequencia)

update(0, 2, frequencia, 1, 0, len(V)-1)
print(S)

frequencia = query(0, 1, 1, 0, len(V)-1)[1]

print(S)


print(frequencia)






