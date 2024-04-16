#Questão A
a = int(input())
s = input()
s = f"b{s}b"
ans =  0
for i in range(2, a+2):
    if((s[i] == 'a' and s[i-1] == 'a')or(s[i] == 'b' and s[i-1] == 'a' and s[i-2] == 'a')):
        ans+=1
print(ans)
