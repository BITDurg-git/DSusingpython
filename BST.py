class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  

def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)

def minValueNode( node): 
    current = node 
    # loop down to find the leftmost leaf 
    while(current.left is not None): 
        current = current.left  
    return current  

def deleteNode(root, key): 
  
    # Base Case 
    if root is None: 
        return root  
  
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    if key < root.val: 
        root.left = deleteNode(root.left, key) 
  
    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
    elif(key > root.val): 
        root.right = deleteNode(root.right, key) 
  
    # If key is same as root's key, then this is the node 
    # to be deleted 
    else: 
          
        # Node with only one child or no child 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
  
        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
        temp = minValueNode(root.right) 
  
        # Copy the inorder successor's content to this node 
        root.val = temp.val
  
        # Delete the inorder successor 
        root.right = deleteNode(root.right , temp.val) 
  
  
    return root  
  

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right)
        

def preorder(root): 
    if root:
        print(root.val) 
        preorder(root.left) 
        preorder(root.right)

def postorder(root): 
    if root: 
        postorder(root.left) 
        postorder(root.right)
        print(root.val)
        
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 
  
# Print inoder traversal of the BST 
print("inorder traversal is:")
inorder(r)
print("preorder traversal is:")
preorder(r)
print("postorder traversal is:")
postorder(r)
deleteNode(r,30)
print("inorder traversal is:")
inorder(r)
