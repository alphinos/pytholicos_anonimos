#APOS UM MÊS RETORNAMOS MAIS FORTES _> Daqui a um mês eu termino, eu prometo

N, Q = map( int, input().split() )

V = [ 1 for _ in range( N ) ]

S = [0 for _ in range(4*N)]
lazy = [0 for i in range(4*N)]

freqs = { 1 : n for n in range( N ) }

#Build
def freq(l, r):
    # L_k = set(l.keys())
    # R_k = set(r.keys())

    # cu = l.keys() + r.keys()
    # for e in cu:
    #     pass

    # freq_dict = {}
    # if L_k == R_k:
    #     for k in L_k:
    #         if not(L_k[k] & R_k[k]):
    #             freq_dict[k] = L_k[k] | R_k[k]
    #         else:
    #             uniao = L_k[k] | R_k[k]
    #             interc = L_k[k] & R_k[k]
    #             freq_dict[k] = (uniao - interc)
    #             freq_dict[k+1] = interc
    
                
                
            
    if l[1] & r[1]:
        return (l[0]+r[0], l[1] & r[1])


    if l[0] == r[0] and not(l[1] & r[1]):
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
        if( p != 1):
            S[p] = ( S[p][0], {valor + v for valor in S[p][1]})
        else:
            S[p] = ( S[p][0], S[p][1] + v)

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

build(1, 0, N-1)

for _ in range( Q ):
    a, b = map( int, input().split())
    print(S)
    frequencia = query(a, b, 1, 0, N-1)[1]
    update(a, b, frequencia, 1, 0, N-1)
    print(S)



print(S)





















    


