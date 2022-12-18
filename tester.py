
import avl_template_new

AVLNode = avl_template_new.AVLNode

n03 = AVLNode(3)
n05 = AVLNode(5)
n08 = AVLNode(8)
n10 = AVLNode(10)
n17 = AVLNode(17)
n20 = AVLNode(20)

n10.right = n20
n10.left = n05
n05.left = n03
n05.right = n08
n20.left = n17
n03.parent=n05
n08.parent=n05
n05.parent=n10
n17.parent=n20
n20.parent=n10
n10.parent = AVLNode('TEST NODE')

n03.left=AVLNode(-1)
n03.right=AVLNode(-1)
n17.left=AVLNode(-1)
n17.right=AVLNode(-1)
n08.right=AVLNode(-1)
n08.left=AVLNode(-1)
n20.right=AVLNode(-1)
tree = AVLTreeList()


tree.root = n10



returned =tree.successor(n03).value
print('return:')
print(returned)