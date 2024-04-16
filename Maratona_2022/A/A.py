#Questão A
a = int(input())
s = input()
s = f"b{s}b" #Mesma string da entrada com 'b' no inicio e fim
ans =  0
for i in range(2, a+2): #For do segundo elemento até o ultimo da string
    #Quando tivermos a subpaalbra 'aa' ou 'aab' contaremos como um a. Ao final a contagem será correta
    if((s[i] == 'a' and s[i-1] == 'a')or(s[i] == 'b' and s[i-1] == 'a' and s[i-2] == 'a')):
        ans+=1
print(ans)
