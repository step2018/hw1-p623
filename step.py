Ans=[]
l=list(input("小文字で入力してください"))
l.sort()

dictionaryWords=open("dictionary.words.txt","r")
for line in dictionaryWords:
    k=list(line)
    del k[len(k)-1]
    A=""
    for K in k:
        K.lower
        A+=K
    k.sort()

    if k==l:
        Ans.append(A)

print(Ans)