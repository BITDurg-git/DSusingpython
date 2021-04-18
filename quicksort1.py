def swap(a,i,j):
    a[i],a[j]=a[j],a[i]

def quicksort(partition,left,right):
    if(left<right):
        pivot=partition[left]
        i=left
        j=right
        print()
        print("pivot:",pivot)
        while(True):
            while(partition[i]<=pivot):
                i=i+1
                print("new i:",i)
            while(partition[j]>pivot):
                j=j-1
                print("new j:",j)
            if(i<j):
                swap(partition,i,j)
                print(partition)
            if( i>j):
                break
    
        swap(partition,left,j)
        print("array after pivot swap:")
        print(a)
        quicksort(partition,left,j-1)
        quicksort(partition,j+1,right)
       


a= [8,1,5,4,4,10,2,8,2,9,4,1,9]
l=len(a)-1
print(l)
quicksort(a,0,l)
print("\n After Sorting \n")
print(a)


