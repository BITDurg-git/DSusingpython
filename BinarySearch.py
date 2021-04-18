arr=[0,1,2,3,4]
low=0
high=len(arr)
num=int(input("Enter element to be searched"))
while low<=high:
    mid=int((low+high)/2)
    if num==arr[mid]:
        print("Num is present at index ",mid)
        break
    elif  arr[mid]<num:
        low=mid+1
    else:
        high=mid-1
