def heapify(arr, n):  
    for i in range(n):
        # if child is bigger than parent  
        if arr[i] > arr[int((i - 1) / 2)]: 
            j = i
            # swap child and parent until parent is smaller  
            while arr[j] > arr[int((j - 1) / 2)]: 
                (arr[j],arr[int((j - 1) / 2)]) = (arr[int((j - 1) / 2)],arr[j]) 
                j = int((j - 1) / 2) 

arr=[4,10,3,5,1]
heapify(arr,len(arr))
print(arr)
