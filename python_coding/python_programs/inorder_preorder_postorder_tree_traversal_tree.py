# Inorder , preorder and postorder traversal of a binary tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('---inorder traversal---')
inorder(root)
print('---preorder traversal---')
preorder(root)
print('---postorder traversal---')
postorder(root)
