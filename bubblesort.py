a=[7,4,5,2]
for i in range((len(a)-1),0,-1):
    for j in range(0,i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
    print(a)
