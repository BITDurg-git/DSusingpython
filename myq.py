arr=[0,0,0]
amax=3
global front,rear
front=rear=-1
def enq(item):
    global rear,front,arr

    #overflow condition
    if front==rear+1:
        print("overflow")
        return

    #case of only 1 element
    elif front==rear==-1:
        front=front+1
        rear=rear+1
        arr[rear]=item
        print("Element inserted at location ",rear," is ",item)
        print("Array is:",arr)

    else:
        #rear is at end
        if rear==amax-1:
            rear=0
            arr[rear]=item
            print("Element inserted at location ",rear," is ",item)
            print("Array is:",arr)

        #general case
        else:
            rear=rear+1
            arr[rear]=item
            print("Element inserted at location ",rear," is ",item)
            print("Array is:",arr)


def deq():
    global front,rear,arr

    #underflow condition
    if rear==-1:
        print("Underflow")
        return

    #case of only 1 element at beginning
    elif front==rear==0:
        print("Element removed from location ",front," is ",arr[front])
        arr[front]=0
        front=rear=-1

    #case of only 1 element anywhere
    elif front==rear:
        print("underflow")
        front=rear=-1

    else:
        if front==amax-1:
            print("Element removed from location ",front," is ",arr[front])
            arr[front]=0
            print("Array is:",arr)
            front=0

        else:
            print("Element removed from location ",front," is ",arr[front])
            arr[front]=0
            front=front+1
            print("Array is:",arr)
enq(2)
enq(6)
enq(7)
deq()
enq(9)
deq()
deq()
deq()
deq()
enq(8)
enq(3)
enq(1)
enq(5)
deq()
deq()
deq()
