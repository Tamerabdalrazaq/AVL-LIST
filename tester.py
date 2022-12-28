import random
import avl_template_new

AVLNode = avl_template_new.AVLNode
AVLTreeList = avl_template_new.AVLTreeList

def test_successor_predecessor():
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

    n03.left=AVLNode(-1)
    n03.right=AVLNode(-1)
    n17.left=AVLNode(-1)
    n17.right=AVLNode(-1)
    n08.right=AVLNode(-1)
    n08.left=AVLNode(-1)
    n20.right=AVLNode(-1)
    tree = AVLTreeList()
    tree.root = n10
    assert tree.successor(n03) == n05
    assert tree.successor(n05) == n08
    assert tree.successor(n08) == n10
    assert tree.successor(n10) == n17
    assert tree.successor(n17) == n20
    assert tree.successor(n20) is None
    assert tree.predecessor(n03) is None
    assert tree.predecessor(n05) == n03
    assert tree.predecessor(n08) == n05
    assert tree.predecessor(n10) == n08
    assert tree.predecessor(n17) == n10
    assert tree.predecessor(n20) == n17


def inserttest():
    tree=AVLTreeList()
    tree.insert(0, 10)
    tree.insert(0, 5)
    tree.insert(0, 3)
    tree.insert(2, 8)
    tree.insert(4, 20)
    tree.insert(4,17)
    tree.insert(6, 18)
    tree.insert(0, -2)
    tree.insert(0, -4)
    tree.insert(0, -6)
    print('____________________________')
    print(tree.getRoot().getLeft().getLeft().getLeft().getLeft().getLeft())
    print(tree.getRoot().getLeft().getLeft().getLeft().getLeft())
    print(tree.getRoot().getLeft().getLeft().getLeft())
    print(tree.getRoot().getLeft().getLeft())
    print(tree.getRoot().getLeft())
    print(tree.getRoot().getLeft().getRight())
    print(tree.getRoot())
    print(tree.getRoot().getRight().getLeft())
    print(tree.getRoot().getRight())


def test_rotation():
    tree=AVLTreeList()
    tree.insert(0,0)
    tree.insert(0,0)
    tree.insert(0, 1)
    tree.insert(0, 2)
    tree.insert(3,3)
    tree.insert(2,4)
    tree.insert(3,5)
    # tree.insert(0, 0)
    # tree.insert(0,0)
    # tree.insert(0,1)
    # tree.insert(1,2)
    # tree.insert(1,3)
    # tree.insert(2,4)

    # tree.insert(0,2)
    # tree.insert(2,3)
    # tree.insert(0,4)
    # tree.insert(2,5)
    # tree.insert(4,6)
    # tree.insert(5,7)

    # tree.insert(0, 2)
    # tree.insert(0, 3)
    # tree.insert(0, 4)
    # tree.insert(0, 5)
    # x=tree.insert(0, 6)

    print('____________________________')
    print('____________________________')
    print('____________________________')
    print(tree.size)
    print(tree.getRoot())
    print(tree.getRoot().getLeft())
    print(tree.getRoot().getRight())
    print(tree.getRoot().getLeft().getLeft())
    print(tree.getRoot().getLeft().getRight())
    print("retrieve:")
    print(tree.retrieve(2))
    print("number of rotations")
    #print(x)
    avl_template_new.printTree(tree.getRoot())
    print(tree.getRoot().getLeft().isRealNode())

def test_2():
    tree=AVLTreeList()
    list = []
    n =10
    tree.insert(0, 0)
    list.insert(0, 0)
    for i in range(0, n):
        index = random.randrange(len(list))
        print('inserting ' + str(i) + ' at ' + str(index))
        list.insert(index, i)
        tree.insert(index, i)

    print('__________________')
    print('__________________')
    print('final tree:')
    avl_template_new.printTree(tree.root)
    print('final List:')
    print(list)
    print('__________________')
    print('__________________')

    for i in range(1,len(list)):
        expected = list[i]
        returned = tree.retrieve(i).value
        assert (list[i] == tree.retrieve(i).value), print_err(i, expected, returned)
        def print_err(i, e, r):
            print("ERROR!")
            print("index: " +str(i))
            print("expected: " +str(e))
            print("returned: " +str(r))
    



# test_successor_predecessor()
# inserttest()
#test_rotation()
for i in range(60):
    test_2()
    print('***********************')
