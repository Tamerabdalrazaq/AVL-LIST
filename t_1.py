import math
import random
import avl_template_new

AVLNode = avl_template_new.AVLNode
AVLTreeList = avl_template_new.AVLTreeList
atl = avl_template_new.arrayToList
print_tree = avl_template_new.printTree

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
        rotations += _del(index, i)
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
    

    for i in range(n//4):
        index1 = random.randrange(tree.getSize())
        rotations += _ins(index1, i)
        index2 = random.randrange(tree.getSize())
        rotations += _del(index2)

    return rotations


for i in range(7, 11):
    print('**********************************************')
    print('i = ' + str(i))
    n = 1500 * (2**i)
    print('Random Insert for size: ' + str(n))
    print(random_isert(n))
    print('Random Delete for size: ' + str(n))
    print(random_isert(n))
    print('Random Insert_Delete for size: ' + str(n))
    print(random_isert(n))