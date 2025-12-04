#CREATION AND INSERTION
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


root=TreeNode(13)
node7=TreeNode(7)
node15=TreeNode(15)
node3=TreeNode(3)
node8=TreeNode(8)
node14=TreeNode(14)
node19=TreeNode(19)
node18=TreeNode(18)

root.left=node7
root.right=node15

node7.left=node3
node7.right=node8

node15.left=node14
node15.right=node19

node19.left=node18


#TRAVERSAL
def in_order(node):
    if node is None:
        return None
    in_order(node.left)
    print(node.data,end=" ")
    in_order(node.right)

def pre_order(node):
    if node is None:
        return None
    print(node.data, end=" ")
    pre_order(node.left)
    pre_order(node.right)

def post_order(node):
    if node is None:
        return None
    post_order(node.left)
    post_order(node.right)
    print(node.data, end=" ")

# in_order(root)
# print()
# pre_order(root)
# print()
# post_order(root)
# print()

#SEARCH
def search(node,data):
    if node is None:
        return None
    elif node.data == data:
        return node
    elif node.data<data:
        search(node.right,data)
    else:
        search(node.left, data)

print("FOUND" if search(root,33) else "NOT FOUND")  #search(Tree_root,Search_Element)

#INSERTION
def insert(node,data):
    if node is None:
        return TreeNode(data)
    else:
        if data<node.data:
            node.left = insert(node.left,data)
        elif data>node.data:
            node.right = insert(node.right,data)
    return node

insert(root,6) #insert(root_node,data_to_insert)
# in_order(root)


#DELETION
#for deletion we have 3 conditions
# 1.if node is leaf node just remove the node
# 2.if node have a child node (only 1) delete the node and make parent of that node to point to its child
# 3.if node is node ha two child nodes: find lowest element in its right subtree. replace node with minimum one

def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.data

def delete(node, data):
    if not node:
        return None

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # node with 0 or 1 child
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp
        # node with 2 children
        node.data = minValue(node.right)
        node.right = delete(node.right, node.data)

    return node

root = delete(root, 15)   # safer way
in_order(root)
print()



