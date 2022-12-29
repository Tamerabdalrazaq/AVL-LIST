# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1  # Balance factor
        self.size = 1

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        return self.left

    def getSize(self):
        return self.size

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        return self.height

    def getBF(self):
        return self.getLeft().getHeight() - self.getRight().getHeight()

    """
    @type size: int
    """

    def setSize(self, size):
        self.size = size

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node
        return None

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node
        return None

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node
        return None

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value
        return None

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h
        return None

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        return self.right is not None and self.left is not None

    def __str__(self) -> str:
        return ('value: ' + str(self.value) + '| isReal: '
                + str(self.isRealNode()) + '| size: ' + str(self.size) + '| height: ' + str(self.getHeight()))

    def copy_from(self, y):
        self.setParent(y.getParent())
        self.setLeft(y.getLeft())
        y.getLeft().setParent(self)
        self.setRight(y.getRight())
        y.getRight().setParent(self)
        self.setSize(y.getSize())
        self.setHeight(y.getHeight())
        if (y.getParent() is not None):
            y.updatechildforpar(self)

    def updatechildforpar(self, new_node):
        if (self.getParent().getLeft() == self):
            self.getParent().setLeft(new_node)
        if (self.getParent().getRight() == self):
            self.getParent().setRight(new_node)


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.size = 0
        self.root = None
        self.first_node = None
        self.last_node = None

    # add your fields here
    def getSize(self):
        if(self.root is None): return 0
        return self.root.getSize()

    def setSize(self, size):
        self.root.setSize(size)
        self.size=size

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return None

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        return self.retrieve_rec(self.root, i)

    def retrieve_rec(self, node, i):
        if (i == 0):
            if (node.getLeft().isRealNode() == False):
                return node
        if (i == node.getLeft().getSize()):
            return node
        if (node.getLeft().isRealNode() and i < node.getLeft().getSize()):
            return self.retrieve_rec(node.getLeft(), i)
        if (node.getRight().isRealNode() and i >= node.getLeft().getSize() + 1):
            return self.retrieve_rec(node.getRight(), i - (node.getLeft().size + 1))
        return None

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    # UNFINISHED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # TODO: Re-arrange functions structure
    def insert(self, i, val):
        new_node = create_leaf(val)
        if i == 0:
            self.first_node = new_node
        if (i == self.getSize()):
            self.last_node = new_node
        if (self.root is None):
            self.root = new_node
            self.size += 1
            return 0

        numofrot = self.insert_rec(self.root, i, new_node)
        self.size += 1
        # printTree(self.root)
        return numofrot

    def insert_rec(self, node, i, new_node):
        if (i == 0):
            if (node.getLeft().isRealNode() == False):
                new_node.setParent(node)
                node.setSize(node.getSize() + 1)
                node.setLeft(new_node)
                return self.series_of_actions(new_node)
        if (i >= node.getLeft().getSize() + 1):
            if (node.getRight().isRealNode() == False):
                new_node.setParent(node)
                node.setSize(node.getSize() + 1)
                node.setRight(new_node)
                return self.series_of_actions(new_node)

        if (node.getLeft().isRealNode() and i <= node.getLeft().getSize()):
            return self.insert_rec(node.getLeft(), i, new_node)
        if (node.getRight().isRealNode() and i >= node.getLeft().getSize() + 1):
            return self.insert_rec(node.getRight(), i - (node.getLeft().size + 1), new_node)
        if (node.getRight().isRealNode() == False and i >= node.getLeft().getSize() + 1):
            new_node.setParent(node)
            node.setSize(node.getSize() + 1)
            node.setRight(new_node)
            return self.series_of_actions(new_node)

        node.setSize(node.getSize() + 1)

    # TODO need to split to height, more actions...

    def series_of_actions(self, new_node):
        numofrot = self.maintain_AVL(new_node)
        return numofrot

    def maintain_AVL(self, new_node):
        # n = new_node.getParent()
        n = new_node
        numofrot = 0
        while (True):
            # x = n.getLeft().getHeight()
            # y = n.getRight().getHeight()
            # height_changed = max(x, y) + 1 != n.getHeight()
            # if (height_changed):
            #     n.setHeight(max(x, y) + 1)
            BF = n.getBF()
            if (abs(BF) == 2):
                numofrot = self.rotate(n, BF)
            n.setSize(n.getLeft().getSize() + n.getRight().getSize() + 1)
            n.setHeight((max(n.getLeft().getHeight(), n.getRight().getHeight()) + 1))
            if (n == self.root):
                break
            n = n.getParent()
        return numofrot

    def rotate(self, n, BF):
        c = 0
        if (BF == -2):
            if (n.getRight().getBF() == -1 or n.getRight().getBF() == 0):
                if (self.getRoot() == n):
                    self.setRoot(n.getRight())
                self.rotate_left(n.getRight())
                c += 1
            elif (n.getRight().getBF() == 1):
                n_right_left = n.getRight().getLeft()
                if (self.getRoot() == n):
                    self.setRoot(n_right_left)
                self.rotate_right(n_right_left)
                self.rotate_left(n_right_left)
                c += 2
        else:
            if (n.getLeft().getBF() == 1 or n.getLeft().getBF() == 0):
                if (self.getRoot() == n):
                    self.setRoot(n.getLeft())
                self.rotate_right(n.getLeft())
                c += 1
            elif (n.getLeft().getBF() == -1):
                n_left_right = n.getLeft().getRight()
                if (self.getRoot() == n):
                    self.setRoot(n_left_right)
                self.rotate_left(n_left_right)
                self.rotate_right(n_left_right)
                c += 2
        return c

    def rotate_right(self, n):
        newleftforparent = n.getRight()
        parent = n.getParent()
        if (parent is not None):
            n.setParent(parent.getParent())
        if (n.getParent() != None):
            if (n.getParent().getLeft() == parent):
                n.getParent().setLeft(n)
            if (n.getParent().getRight() == parent):
                n.getParent().setRight(n)
            # n.getParent().setHeight(max(n.getParent().getRight().getHeight(), n.getParent().getLeft().getHeight()) + 1)
            # n.getParent().setSize(n.getParent().getRight().getSize() + n.getParent().getLeft().getSize() + 1)
        n.setRight(parent)
        parent.setParent(n)
        parent.setLeft(newleftforparent)
        newleftforparent.setParent(parent)
        parent.setHeight(max(parent.getRight().getHeight(), parent.getLeft().getHeight()) + 1)
        parent.setSize(parent.getRight().getSize() + parent.getLeft().getSize() + 1)
        n.setSize(n.getRight().getSize() + n.getLeft().getSize() + 1)
        n.setHeight(max(n.getRight().getHeight(), n.getLeft().getHeight()) + 1)

    def rotate_left(self, n):
        newrightforparent = n.getLeft()
        parent = n.getParent()
        if (parent is not None):
            n.setParent(parent.getParent())
        if (n.getParent() != None):
            if (n.getParent().getLeft() == parent):
                n.getParent().setLeft(n)
            if (n.getParent().getRight() == parent):
                n.getParent().setRight(n)
            # n.getParent().setHeight(max(n.getParent().getRight().getHeight(), n.getParent().getLeft().getHeight()) + 1)
            # n.getParent().setSize(n.getParent().getRight().getSize() + n.getParent().getLeft().getSize() + 1)
        n.setLeft(parent)
        parent.setParent(n)
        parent.setRight(newrightforparent)
        newrightforparent.setParent(parent)
        parent.setHeight(max(parent.getRight().getHeight(), parent.getLeft().getHeight()) + 1)
        parent.setSize(parent.getRight().getSize() + parent.getLeft().getSize() + 1)
        n.setSize(n.getRight().getSize() + n.getLeft().getSize() + 1)
        n.setHeight(max(n.getRight().getHeight(), n.getLeft().getHeight()) + 1)

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        if (i >= self.size or i < 0):
            return -1
        node = self.retrieve(i)
        if(i == 0):
            self.first_node = self.successor(node)
        if(i == self.getSize() - 1):
            self.last_node = self.predecessor(node)
        # if (node is None):
        #     return -1
        if (node.getRight().isRealNode() == False and node.getLeft().isRealNode() == False):
            if (self.root != node):
                if (node.getParent().getRight() == node):
                    node.getParent().setRight(node.getRight())
                if (node.getParent().getLeft() == node):
                    node.getParent().setLeft(node.getRight())
            else:
                self.size = 0
                self.root = None
                self.first = None
                self.last = None
        elif (node.getRight().isRealNode() == True and node.getLeft().isRealNode() == True):
            successor = self.successor(node)
            self.switch_nodes(successor, node)
            self.delete(i + 1)
        elif (node.getRight().isRealNode() == False):
            new_node = node.getLeft()
            new_node.setParent(node.getParent())
            if (self.root != node):
                if (node.getParent().getRight() == node):
                    node.getParent().setRight(new_node)
                if (node.getParent().getLeft() == node):
                    node.getParent().setLeft(new_node)
            else:
                self.root = new_node
        elif (node.getLeft().isRealNode() == False):
            new_node = node.getRight()
            new_node.setParent(node.getParent())
            if (self.root != node):
                if (node.getParent().getRight() == node):
                    node.getParent().setRight(new_node)
                if (node.getParent().getLeft() == node):
                    node.getParent().setLeft(new_node)
            else:
                self.root = new_node
        #self.setSize(self.getSize()-1)
        if (node.getParent() is not None):
            return self.maintain_AVL(node.getParent())
        return 0

    def switch_nodes(self, x, y):
        if (self.root == x or self.root == y):
            root = y if self.root == x else x
            self.setRoot(root)
        temp = AVLNode(None)
        temp.copy_from(x)
        x.copy_from(y)
        y.copy_from(temp)
        # printTree(self.root)

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return self.first

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return self.last

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        return None

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return None

    """sort the info values of the list

    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        return None

    """permute the info values of the list 

    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """

    def permutation(self):
        return None

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        h1 = self.root.getHeight()
        h2 = lst.root.getHeight()
        h = min(h1, h2)
        res = 0
        goleft = True
        node = lst.root
        indextodelete = self.getSize()
        if (h1 > h2):
            goleft = False
            node = self.root
        while (node.getHeight() > h):
            if (goleft == True):
                node = node.getLeft()
            else:
                node = node.getRight()
        newnode = AVLNode("todelete")
        if (goleft == True):
            newnode.setLeft(self.root)
            newnode.setRight(node)
            newnode.setParent(node.getParent())
            if (node.getParent() is not None):
                node.getParent().setLeft(newnode)
            node.setParent(newnode)
        else:
            indextodelete = self.getSize() - node.getRight().getSize()
            newnode.setRight(lst.root)
            newnode.setLeft(node)
            newnode.setParent(node.getParent())
            if (node.getParent() is not None):
                node.getParent().setRight(newnode)
            node.setParent(newnode)
        newnode.setHeight(h + 1)
        newnode.setSize(newnode.getLeft().getSize() + newnode.getRight().getSize() + 1)
        self.updateroot(newnode)
        self.setSize(self.getSize() + lst.getSize() + 1)
        if (newnode.getParent() is not None and abs(newnode.getParent().getBF()) > 1):
            res = abs(newnode.getParent().getBF())
            self.maintain_AVL(newnode)
        print(indextodelete)
        self.delete(indextodelete)
        return res

    def updateroot(self, node):
        while node.getParent() is not None:
            node = node.getParent()
        self.setRoot(node)

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        return None

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root

    def setRoot(self, root):
        self.root = root

    # TODO: Handle min, max  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def successor(self, node):
        if (node.right.isRealNode()):
            x = node.right
            while (x.left.isRealNode()):
                x = x.left
            return x
        else:
            x = node
            while (x != self.getRoot() and x == x.parent.right):
                x = x.parent
            return x.parent

    def predecessor(self, node):
        if (node.left.isRealNode()):
            x = node.left
            while (x.right.isRealNode()):
                x = x.right
            return x
        else:
            x = node
            while (x != self.getRoot() and x == x.parent.left):
                x = x.parent
            return x.parent


def printTree(node, level=0):
    if node is not None:
        printTree(node.right, level + 1)
        print(' ' * 8 * level + '-> ' + str(node.value) + "{" + str(node.getSize()) + "," + str(node.getHeight()) + "}")
        printTree(node.left, level + 1)


def create_leaf(val):
    leaf = AVLNode(val)
    l_virtual = AVLNode(None)
    l_virtual.setSize(0)
    r_virtual = AVLNode(None)
    r_virtual.setSize(0)
    leaf.right = r_virtual
    leaf.left = l_virtual
    leaf.setHeight(0)
    return leaf


def arrayToList(arr, a, b, parent) -> AVLTreeList:
    tree = AVLTreeList()
    # print(str(a)+ ', ' + str(b))
    med = (a + b) // 2
    root = create_leaf(arr[med])
    root.setParent(parent)
    tree.setRoot(root)
    tree.size = 1

    if (a == b): return tree

    left_tree, right_tree = None, None
    if (med > a):
        left_tree = arrayToList(arr, max(0, a), max(med - 1, 0), root)
        root.setLeft(left_tree.getRoot())
    if (med < b):
        right_tree = arrayToList(arr, min(med + 1, len(arr) - 1), min(b, len(arr) - 1), root)
        root.setRight(right_tree.getRoot())

    h_1 = -1 if left_tree is None else left_tree.getRoot().getHeight()
    h_2 = -1 if right_tree is None else right_tree.getRoot().getHeight()
    s_1 = 0 if left_tree is None else left_tree.size
    s_2 = 0 if right_tree is None else right_tree.size

    root.setSize(s_1 + s_2 + 1)
    root.setHeight(max(h_1, h_2) + 1)
    tree.size = s_1 + s_2 + 1

    return tree
