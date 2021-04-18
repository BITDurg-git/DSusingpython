class Node: 

    def __init__(self, data): 
        self.data = data 
        self.next = None 


class LinkedList: 

    def __init__(self): 
        self.head = None

    def listprint(self):
        printval=self.head
        while printval is not None:
            print(printval.data)
            printval=printval.next

    def search(self):
        num=int(input("Enter num to be searched:"))
        ref=self.head
        flag=0
        while ref is not None:
            if ref.data==num:
                print("num is found")
                flag=1
                break
            ref=ref.next
        if flag==0:
            print("Num is not found")

    def insertatbeg(self):
        num=int(input("Enter number to be inserted"))
        Newnode=Node(num)

        #list is empty
        if self.head==None:
            print("list is empty")

        #General Case
        Newnode.next=self.head
        self.head=Newnode

    def insertatend(self):
        num=int(input("Enter num to be inserted"))
        Newnode=Node(num)
        
        #list is empty
        if self.head==None:
            print("list is empty")
            Newnode.next=self.head
            self.head=Newnode
            
        #General Case
        else:
            ref=self.head
            while ref.next:
                ref=ref.next
            ref.next=Newnode

    def insertatmid(self):
        num=int(input("Enter num to be inserted"))
        Newnode=Node(num)
        loc=int(input("Enter num after which you want to insert"))

        #list is empty
        if self.head==None:
            print("list is empty")
            Newnode.next=None
            self.head=Newnode
            return

        #general case
        ref=self.head
        while ref is not None:
            prev=ref
            if ref.data==loc:
                Newnode.next=ref.next
                ref.next=Newnode
                return
            
            ref=ref.next
        
        #if num is not in list it should be added at the end
        if ref==None:
            print("Num is not found")
            Newnode.next=None
            prev.next=Newnode
            

            

    def delete(self):
        num=int(input("Enter num to delete"))
        ref=self.head
        prev = self.head
        if ref==None:
            print("list is empty")
            return

        if self.head.data==num:
           self.head = self.head.next
           return

        
        while ref is not None:
            if ref.data==num:
                break
            prev=ref
            ref=ref.next
            
        if ref!=None:
            prev.next=ref.next
        else:
            print("Num is not found")


    def options(self):
        print("What do you want to do")
        print("1. Print the list")
        print("2. Search")
        print("3. Insert at the beginning")
        print("4. Insert at the end")
        print("5. Insert at the mid")
        print("6. Delete")
        print("7. Exit")
        option=int(input("Enter your option"))
        if option==1:
            llist.listprint()
            llist.options()
        if option==2:
            llist.search()
            llist.options()
        if option==3:
            llist.insertatbeg()
            llist.listprint()
            llist.options()
        if option==4:
            llist.insertatend()
            llist.listprint()
            llist.options()
        if option==5:
            llist.insertatmid()
            llist.listprint()
            llist.options()
        if option==6:
            llist.delete()
            llist.listprint()
            llist.options()
        if option==7:
            exit
    
                


# Code execution starts here 
if __name__=='__main__':

    # Start with the empty list 
    llist = LinkedList() 

    #llist.head = Node(1) 
    #second = Node(2) 
    #third = Node(3)
    #fourth=Node(4)

    #llist.head.next = second; # Link first node with second 
    #second.next = third; # Link second node with the third node
    #third.next=fourth

    llist.options()
    
