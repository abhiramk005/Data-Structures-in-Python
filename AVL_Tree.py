class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left)-getHeight(node.right)

def rightRotate(node):
    print("Right rotate on node",node.data)
    x=node.left
    t2=x.right
    x.right=node
    node.left=t2
    node.height=1+max(getHeight(node.left),getHeight(node.right))
    x.height=1+max(getHeight(x.right),getHeight(x.left))
    return x

def leftRotate(node):
    print("Left rotate on node",node.data)
    y=node.right
    t2=y.left
    y.left=node
    node.right=t2
    node.height=1+max(getHeight(node.left),getHeight(node.right))
    y.height=1+max(getHeight(y.right),getHeight(y.left))
    return y


def insert(node,data):
    if not node:
        return Treenode(data)

    if data<node.data:
        node.left=insert(node.left,data)
    elif data>node.data:
        node.right=insert(node.right,data)
    #height update
    node.height=1+max(getHeight(node.left),getHeight(node.right))
    balance=getBalance(node)

    #Balancing
    #LL
    if balance>1 and getBalance(node.left)>=0:
        return rightRotate(node)

    #RR
    if balance<-1 and getBalance(node.right) <= 0:
        return leftRotate(node)

    #LR
    if balance>1 and getBalance(node.left)<0:
        node.left=leftRotate(node.left)
        return rightRotate(node)

    #RL
    if balance<-1 and getBalance(node.right)>0:
        node.right=rightRotate(node.right)
        return leftRotate(node)

    return node

def in_order(node):
    if node is None:
        return None
    in_order(node.left)
    print(node.data,end=" ")
    in_order(node.right)

#DELETION

def minValueNode(node):
    current=node
    while current.left is not None:
        current=current.left
    return current

def delete(node,data):
    if not node:
        return node

    if data<node.data:
        node.left=delete(node.left,data)
    elif data>node.data:
        node.right=delete(node.right,data)
    else:
        if node.left is None:
            temp=node.right
            node=None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        temp=minValueNode(node.right)
        node.data=temp.data
        node.right=delete(node.right,temp.data)

    if node is None:
        return node
    node.height=1+max(getHeight(node.left),getHeight(node.right))
    balance=getBalance(node)
    #Balancing after  deletion
    # LL
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)
    # RR
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)
    # LR
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    # RL
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    return node


root=None
letters=['C','B','E','A','D','H','G','F']
for letter in letters:
    root=insert(root,letter)
in_order(root)
print("\ndeletion phase\n")
root=delete(root,'G')
in_order(root)




