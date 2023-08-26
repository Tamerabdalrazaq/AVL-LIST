import math
import random
import avl_tree

AVLNode = avl_tree.AVLNode
AVLTreeList = avl_tree.AVLTreeList
atl = avl_tree.arrayToList
print_tree = avl_tree.printTree

def create_list_tree(n):
    tree=AVLTreeList()
    list = []
    tree.insert(0, 0)
    list.insert(0, 0)
    for i in range(1, n):
        index = random.randrange(len(list))
        rand = random.randrange(2**10)
        print('inserting ' + str(i) + ' at ' + str(index))
        list.insert(index, rand)
        tree.insert(index, rand)
    return tree,list

def test_insert_delete(_list, _tree, n):
    def execute_assertions():
        assert(len(list) == tree.getSize())
        for i in range(1,len(list)):
            node = tree.retrieve(i)
            expected = list[i]
            returned = node.value
            assert (list[i] == tree.retrieve(i).value)
            assert node.getBF() <= 1
            assert (i == len(list) - 1 or tree.successor(node).value == list[i+1])
            assert (i == 0 or tree.predecessor(node).value == list[i - 1] )
            # assert(tree.search(returned) == i)
            if(tree.getSize() > 0):
                assert tree.last().value == list[-1]
                assert tree.first().value == list[0]
            else: 
                assert tree.last() == None
                assert tree.first() == None
            def print_err(i, e, r):
                print("ERROR!")
                print("index: " +str(i))
                print("expected: " +str(e))
                print("returned: " +str(r))
    def _ins(index, v):
        print('inserting ' + str(v) + ' at ' + str(index))
        list.insert(index, v)
        tree.insert(index , v)
    def _del(index):
        print('deleting ' + ' at ' + str(index))
        list.pop(index)
        tree.delete(index)

    print('**********************************************************************************')
    tree=AVLTreeList() if _tree is None else _tree
    list = [] if _list is None else _list
    print('______')
    print('______')
    print('final tree:')
    avl_template_new.printTree(tree.root)
    print('final List:')
    print(list)
    print('______')
    print('______')

    execute_assertions()

    for i in range(0, n):
        if(len(list) == 0):
            _ins(0, i)
        else:
            coin = random.randrange(8)
            if(coin <= 5):
                index = random.randrange(len(list))
                _ins(index, i)
            else:
                index = random.randrange(len(list))
                _del(index)

    print('______')
    print('______')
    print('final tree:')
    avl_template_new.printTree(tree.root)
    print('final List:')
    print(list)
    print('______')
    print('______')


    execute_assertions()
            
        
def test_concat():
    x=create_list_tree(5)
    y=create_list_tree(1)
    tree1=x[0]
    list1=x[1]
    tree2=y[0]
    list2=y[1]
    print("***************tree1******************")
    avl_template_new.printTree(tree1.root)
    print(list1)
    print(tree1.getSize())
    print("***************tree2******************")
    avl_template_new.printTree(tree2.root)
    print(list2)
    print(tree2.getSize())
    print("***************after concat******************")
    tree1.concat(tree2)
    avl_template_new.printTree(tree1.root)
    test_insert_delete(list1+list2,tree1,20)

def test_concat2(n):
    rand1 = random.randrange(1, n)
    rand2 = random.randrange(1, n)

    tree1, list1 = create_list_tree(rand1)
    tree2, list2 = create_list_tree(rand2)
    print('...............................................................')
    print_tree(tree1.getRoot())
    print('\n\n\n')
    print_tree(tree2.getRoot())
    print(list1)
    print(list2)
    print('...............................................................\n\n')
    tree1.concat(tree2)
    list = list1 + list2
    test_insert_delete(list, tree1, 20)

    
def test_arrayToList():
    lst = list(range(0,100))
    tree = atl(lst)
    print_tree(tree.getRoot())
    print(tree.retrieve(6).parent)

    for i in range(0,len(lst)):
        expected = lst[i]
        returned = tree.retrieve(i).value
        print(expected, returned)
        assert (lst[i] == tree.retrieve(i).value), print_err(i, expected, returned)
        def print_err(i, e, r):
            print("ERROR!")
            print("index: " +str(i))
            print("expected: " +str(e))
            print("returned: " +str(r))
    test_insert_delete(lst, tree, 200)

def test_listToArray():
    tree, arr = create_list_tree(20)
    _arr = tree.listToArray()
    assert arr == _arr
    

def test_permutations():
    tree, arr = create_list_tree(20)
    shuffled = tree.permutation()
    print('Before: ')
    print_tree(tree.getRoot())
    print('After: ')
    print_tree(shuffled.getRoot())
    assert shuffled.getSize() == tree.getSize()
    
def test_sorting():
    tree, arr = create_list_tree(70)
    sortedlist = tree.sort()
    print('Before: ')
    print_tree(tree.getRoot())
    print('After: ')
    print_tree(sortedlist.getRoot())
    print(sortedlist.getRoot())
    print(sorted(arr))
    print(sortedlist.listToArray())
    assert (sorted(arr) == sortedlist.listToArray())
    assert sortedlist.getSize() == tree.getSize()





# for i in range(100):
#     for k in range(math.ceil(10 + 1000/(i+1))):
#         test_insert_delete(None, None, i)

for i in range(100):
  test_concat2(40)

for i in range(100):
    for k in range(math.ceil(100 + 1000/(i+1))):
        test_insert_delete(None, None, i)

