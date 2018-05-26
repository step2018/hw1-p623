Ans=[]
l=list(input("小文字で入力してください"))
i=0
while i<len(l):
    if l[i]=="q":
        l.remove(l[i+1])
        l[i]="qu"
    else:
        pass
    i+=1
l.sort()
print(l)

dictionaryWords=open("dictionary.words.txt","r")
for line in dictionaryWords:
    k=list(line)
    del k[len(k)-1]
    m=0
    while m<len(k):
        if k[m]=="q":
            k.remove(k[m+1])
            k[m]="qu"
        else:
            pass
        m+=1

    A=""
    for K in k:
        K.lower
        A+=K
    k.sort()

    if k==l:
        Ans.append(A)

print(Ans)