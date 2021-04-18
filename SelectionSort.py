a=[64,25,12,22,11]
for j in range(0,len(a)):
    minimum=a[j]
    for i in range(j+1,len(a)):
       if a[i]< minimum:
            minimum=a[i]
            loc=i
    #print("Minimum in ",j," iteration",minimum)
    a[j],a[loc]=a[loc],a[j]
    print("After finding ",j," minimum element array is:",a)

