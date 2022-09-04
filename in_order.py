from node import root


def in_order(root):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
'''


print("\nInorder traversal\n")
in_order(root)
