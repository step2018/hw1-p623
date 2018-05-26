Ans=[]
point=[]
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
    pt=0
    for K in k:
        K.lower
        A+=K
        if K=="j" or K=="k" or K=="qu" or K=="x" or K=="z":
            pt+=3
        elif K=="c" or K=="f" or K=="h" or K=="l" or K=="m" or K=="p" or K=="v" or K=="w" or K=="y":
            pt+=2
        else:
            pt+=1
        
    k.sort()

    li=[]
    for lis in l:
        li.append(lis)
    x=0
    for moji in k:
        if moji in li:
            if moji==k[len(k)-1]:
                Ans.append(A)
                point.append(pt)
            else:
                li.remove(moji)
        else:
            break


dic={}
y=0
while y<len(Ans):
    dic[Ans[y]]=point[y]
    y+=1

sorted_dic=sorted(dic.items(),key=lambda z:z[1], reverse=True)

for z,v in sorted_dic:
    print(z,v)
