def createstack():
    global stack
    stack=[]

def push(stack,item):
    stack.append(item)
    top=len(stack)
    print(item,"is pushed to stack")

def pop(stack):
    print(stack[len(stack)-1],"is deleted")
    n=stack[len(stack)-1]
    del stack[len(stack)-1]
    top=len(stack)
    return n

def isempty(stack):
    if len(stack)==0:
        print("stack is empty")

def evaluatePostfix(exp):
    for i in exp:
        if i.isdigit():
            push(stack,i)
        else:
            val1 = pop(stack)
            val2 = pop(stack)
            push(stack,str(eval(val2 + i + val1))) 
    return pop(stack) 
      

createstack()
exp = "84/2/1/"
print("postfix evaluation:",evaluatePostfix(exp)) 
    
