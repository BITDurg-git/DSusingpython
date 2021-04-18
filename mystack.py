arr=[0,0,0,0,0]
amax=4
top=-1
def push(item):
    global top,arr
    if top>=amax:
        print("overflow")
        return
    else:
        top=top+1
        arr[top]=item
        print("Element inserted at location ",top," is ",item)
        print("Array is:",arr)

def pop():
    global top,arr
    if top==-1:
        print("Underflow")
        return
    else:
        print("Element popped from location ",top," is ",arr[top])
        arr[top]=0
        top=top-1
        print("Array is:",arr)

push(6)
push(7)
pop()
push(26)
push(8)
push(3)
push(7)
push(9)
pop()
pop()
pop()
pop()
pop()
pop()
