#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  

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
		self.height = -1 # Balance factor
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
		self.left=node
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
		self.parent=node
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
		self.height= h
		return None

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return self.right is not None and self.left is not None
	
	def __str__(self) -> str:
		return ('value: ' + str(self.value) + '| isReal: ' 
		+ str(self.isRealNode()) + '| size: ' +str(self.size))


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
		self.first = None
		self.last = None
		# add your fields here


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
	def insert_rec(self, node, i,val):
		if(i==0):
			if(node.getLeft().isRealNode() == False):
				new_node = create_leaf(val)
				new_node.setParent(node)
				node.setSize(node.getSize() + 1)
				node.setLeft(new_node)
				print(node) 
				print('| <-  |') 
				print(new_node )
				print('----------------')
				return
		if(i==1):
			if(node.getRight().isRealNode()==False):
				new_node = create_leaf(val)
				new_node.setParent(node)
				node.setSize(node.getSize() + 1)
				node.setRight(new_node)
				print(node )
				print('| ->  |') 
				print(new_node) 
				print('----------------')
				return

		if(node.getLeft().isRealNode() and i<=node.getLeft().getSize()):
			return self.insert_rec(node.getLeft(),i,val)
		if(node.getRight().isRealNode() and i>=node.getLeft().getSize()+1):
			return self.insert_rec(node.getRight(),i - (node.getLeft().size + 1),val)
		if(node.getRight().isRealNode()== False and i>=node.getLeft().getSize()+1):
			new_node = create_leaf(val)
			new_node.setParent(node)
			node.setSize(node.getSize() + 1)
			node.setRight(new_node)
			print(node )
			print('| ->  |') 
			print(new_node)
			print('----------------')
			return
			
		node.setSize(node.getSize()+1)
		
	def insert(self, i, val):
		if(self.size == 0):
			node = create_leaf(val)
			self.root = node
			self.size += 1
			return
		new_node = self.insert_rec(self.root,i,val)
		self.size += 1
		return -1
	


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return None

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return None

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
		return None

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
# TODO: Handle min, max 
	def successor(self, node):
		if(node.right.isRealNode()):
			x = node.right
			while (x.left.isRealNode()):
				x = x.left
			return x
		else:
			x = node
			while(x != self.getRoot() and x == x.parent.right):
				x = x.parent
			return x.parent

	def predecessor(self, node):
		if(node.left.isRealNode()):
			x = node.left
			while (x.right.isRealNode()):
				x = x.right
			return x
		else:
			x = node
			while(x != self.getRoot() and x == x.parent.left):
				x = x.parent
			return x.parent


def create_leaf(val):
	leaf = AVLNode(val)
	l_virtual = AVLNode(None)
	r_virtual = AVLNode(None)
	leaf.right = r_virtual
	leaf.left = l_virtual
	return leaf