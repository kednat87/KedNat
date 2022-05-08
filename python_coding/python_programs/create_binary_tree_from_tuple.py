class Treenode():
    ''' Treenode class which identifies a node in a tree .
        key is the root node. left and right are left and right nodes of a tree'''

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def tree_from_tuple(data):
    '''Given a tuple that represents a tree function would create a tree using class Treenode and return the root node'''
    if data is None:
        l = 1
    else:
        try:
            l = len(data)
        except:
            l = 1

    if l == 3:
        node = Treenode(data[1])
        node.left = tree_from_tuple(data[0])
        node.right = tree_from_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = Treenode(data)
    return node


# Input of tree in a tuple format
inp_tuple = ((1, 3, None), 2, ((None, 3, 4,), 5, (6, 7, 8)))
root = tree_from_tuple(inp_tuple)


def print_tree(root):
    ''' Print all the elements in the given tree. Input is root node of the tree'''
    print(root.key)

    if root.left is not None:
        print_tree(root.left)
    else:
        print(None)

    if root.right is not None:
        print_tree(root.right)
    else:
        print(None)


print('------Printing all elements in the tree------')

print_tree(root)


def print_leafs(root):
    '''Identify all the leaf nodes in a tree and append them to list'''
    if root.left is None and root.right is None:
        tree_leaf.append(root.key)
    if root.left is not None:
        print_leafs(root.left)
    if root.right is not None:
        print_leafs(root.right)


print('------Printing all the leaf nodes------')
tree_leaf = []
print_leafs(root)
print(tree_leaf)

tree_inorder = []


def inorder_tree(root):
    if root:
        inorder_tree(root.left)
        print(root.key)
        inorder_tree(root.right)

inorder_tree(root)
