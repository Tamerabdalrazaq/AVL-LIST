import math
import random
import avl_tree
import LinkdList
import time


AVLNode = avl_tree.AVLNode
AVLTreeList = avl_tree.AVLTreeList
atl = avl_tree.arrayToList
print_tree = avl_tree.printTree

def tree_insert_first(n):
    def _ins(index, v):
        curr_rotations = tree.insert(index , v)
        return curr_rotations
    tree=AVLTreeList()

    for i in range(0, n):
        index = 0
        _ins(index, i)
    return tree


def array_insert_first(n):
    def _ins(index, v):
        curr_rotations = arr.insert(index , v)
        return curr_rotations
    arr= []

    for i in range(0, n):
        index = 0
        _ins(index, i)
    return arr


def linked_list_insert_first(n):
    def _ins(index, v):
        curr_rotations = linked_list.addToStart(v)
        return curr_rotations
    linked_list= LinkdList.LinkedList()

    for i in range(0, n):
        index = 0
        _ins(0, i)
    return linked_list

def tree_insert_random(n):
    def _ins(index, v):
        curr_rotations = tree.insert(index , v)
    tree=AVLTreeList()

    for i in range(0, n):
        if(tree.getSize() == 0):
            _ins(0, i)
        index = random.randrange(tree.getSize())
        _ins(index, i)
    return tree


def array_insert_random(n):
    def _ins(index, v):
        curr_rotations = arr.insert(index , v)
        return curr_rotations
    arr= []

    for i in range(0, n):
        if(len(arr) == 0):
            _ins(0, i)
        index = random.randrange(len(arr))
        _ins(index, i)
    return arr

def linked_list_insert_random(n):
    def _ins(index, v):
        curr_rotations = linked_list.addToIndex(index, v)
    linked_list= LinkdList.LinkedList()

    for i in range(0, n):
        if(linked_list.size == 0):
            _ins(0, i)
        index = random.randrange(linked_list.size)
        _ins(index, i)
    return linked_list


def tree_insert_last(n):
    def _ins(index, v):
        curr_rotations = tree.insert(index , v)
        return curr_rotations
    tree=AVLTreeList()

    for i in range(0, n):
        index = tree.getSize() - 1
        _ins(index, i)
    return tree



def array_insert_last(n):
    def _ins(index, v):
        curr_rotations = arr.insert(index , v)
        return curr_rotations
    arr= []

    for i in range(0, n):
        index = len(arr) - 1
        _ins(index, i)
    return arr


def linked_list_insert_last(n):
    def _ins(index, v):
        curr_rotations = linked_list.addToEnd(v)
        return curr_rotations
    linked_list= LinkdList.LinkedList()

    for i in range(0, n):
        index = linked_list.size
        _ins(index, i)
    return linked_list


for i in range(1,11):
    print('**********************first************************')
    print('i = ' + str(i))
    n = 1500 * i

    before = time.time()
    tree = (tree_insert_first(n))
    print('Tree: ' + str(time.time() - before))

    before = time.time()
    array = array_insert_first(n)
    print('Array: ' +str(time.time() - before))

    before = time.time()
    linked_list = linked_list_insert_first(n)
    print('Linked List: ' +str(time.time() - before))

    print('********************last**************************')

    before = time.time()
    tree = (tree_insert_last(n))
    print('Tree: ' + str(time.time() - before))

    before = time.time()
    array = array_insert_last(n)
    print('Array: ' + str(time.time() - before))

    before = time.time()
    linked_list = linked_list_insert_last(n)
    print('LinkedList: ' + str(time.time() - before))

    print('*****************random*****************************')
    before = time.time()
    tree = (tree_insert_random(n))
    print('Tree: ' + str(time.time() - before))

    before = time.time()
    array = array_insert_random(n)
    print('Array: ' + str(time.time() - before))

    before = time.time()
    linked_list = linked_list_insert_random(n)
    print('LinkedList: ' + str(time.time() - before))
