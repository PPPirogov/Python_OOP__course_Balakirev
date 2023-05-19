s =''
answer =''
b =len(s)
#print(b)
a = 0
while  a <  b:
    #print(s[a],a)
    if s[a]!='-':
        answer+=s[a]
    else:
        count = 1
        while a + count != b and s[a+count]=='-':
            count+=1
        a+=count-1
        answer += '-'

    a+=1
print(answer)