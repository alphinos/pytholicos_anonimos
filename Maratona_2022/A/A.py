#Questão A
a = int(input())
s = input()
m = f"b{s}b"
ans =  0
for i in range(2, a+2):
    if((m[i] == 'a' and m[i-1] == 'a')or(m[i] == 'b' and m[i-1] == 'a' and m[i-2] == 'a')):
        ans+=1
print(ans)
