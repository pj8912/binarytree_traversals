from node import root


def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)





print("PreOrder traversal\n")
pre_order(root)

