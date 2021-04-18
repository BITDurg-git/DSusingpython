a=[4,3,2,10,12,1,5,6]
for i in range(1,len(a)):
    key=a[i]
    pos=i
    while pos>0 and a[pos-1]>key:
        a[pos],a[pos-1]=a[pos-1],a[pos]
        pos=pos-1
    #print("After ",i,"iteration:", key, "is been placed at its position.")
    print("Array after placing ",key," in its correct position", a)


        
            
