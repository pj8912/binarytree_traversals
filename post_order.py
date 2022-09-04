from node import root


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)




print("PostOrder Traversal[left,right,root]\n")
post_order(root)
