class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printlist(self):
        printval=self.head
        while printval is not None:
            print(printval.data, end="")
            printval=printval.next
        print()

    def traverse(self):
        ptr=self.head
        while ptr.next is not None:
            ptr=ptr.next
        while ptr.prev is not None:
            print(ptr.data,end="")
            ptr=ptr.prev
        print(ptr.data)

    def insert(self):
        new=Node(55)
        loc=int(input("Enter location"))
        ptr=self.head
        while ptr.data!=loc:
            ptr=ptr.next
        new.next=ptr.next
        new.next.prev=new
        ptr.next=new
        new.prev=ptr
            
            
if __name__== "__main__":

    llist=LinkedList()
    
    First=Node(1)
    llist.head=First
    second=Node(2)
    third=Node(3)
    fourth=Node(4)

    llist.head.next=second
    second.next=third
    third.next=fourth
    fourth.next=None

    fourth.prev=third
    third.prev=second
    second.prev=First
    First.prev=None
    llist.printlist()
    llist.traverse()
    llist.insert()


    
    
