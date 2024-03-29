import math
import random
import avl_tree

AVLNode = avl_tree.AVLNode
AVLTreeList = avl_tree.AVLTreeList
atl = avl_tree.arrayToList
print_tree = avl_tree.printTree

def random_isert(n):
    def _ins(index, v):
        curr_rotations = tree.insert(index , v)
        # print(curr_rotations)
        return curr_rotations

    rotations = 0
    tree=AVLTreeList()
    for i in range(0, n):
        if(tree.getSize() == 0):
            rotations += _ins(0, i)
        index = random.randrange(tree.getSize())
        rotations += _ins(index, i)
    return rotations
    
def random_delete(n):
    def _del(index):
        return tree.delete(index)
    def _ins(index, v):
        return tree.insert(index , v)

    rotations = 0
    tree=AVLTreeList()

    for i in range(0, n):
        if(tree.getSize() == 0):
            rotations += _ins(0, i)
        index = random.randrange(tree.getSize())
        rotations += _ins(index, i)


    for i in range(0, n):
        index = random.randrange(tree.getSize())
        rotations += _del(index)
    return rotations

def random_insert_delete(n):
    def _ins(index, v):
        return tree.insert(index , v)

    def _del(index):
        return tree.delete(index)
    rotations = 0
    tree=AVLTreeList()
    for i in range(0, n//2):
        if(tree.getSize() == 0):
            rotations += _ins(0, i)
        index = random.randrange(tree.getSize())
        rotations += _ins(index, i)

    rotations_2 = 0
    for i in range(n//4):
        index1 = random.randrange(tree.getSize())
        rotations_2 += _ins(index1, i)
        index2 = random.randrange(tree.getSize())
        rotations_2 += _del(index2)

    return (rotations, rotations_2)


for i in range(7,8):
    print('**********************************************')
    print('i = ' + str(i))
    n = 1500 * (2**i)
    print('Random Insert for size: ' + str(n))
    print(random_isert(n))
    print('Random Delete for size: ' + str(n))
    print(random_delete(n))
    print('Random Insert_Delete for size: ' + str(n))
    print(random_insert_delete(n))
