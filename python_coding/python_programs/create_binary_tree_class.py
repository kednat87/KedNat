class TreeNode():

    def __init__(self,key,left=None,right=None):
        self.key = key
        self.left=left
        self.right=right


node5 = TreeNode(5)
node4 = TreeNode(4)
node6 = TreeNode(6)

node5.left = node4
node5.right = node6

print('Printing node 5 elements')
print(node5.key)
print(node5.left)
print(node5.right)


node3 = TreeNode(3)

node4.left = node3
node4.right = None

print('Printing node 4 elements')
print(node4.key)
print(node4.left)
print(node4.right)
