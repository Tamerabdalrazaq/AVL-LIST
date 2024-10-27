# AVL Tree and Linked List Data Structures

This repository contains implementations of AVL Tree and Linked List data structures in Python. The project includes unit tests to ensure the correctness of the implementations.

#### AVL Trees
An AVL Tree is a self-balancing binary search tree (BST) named after its inventors Adelson-Velsky and Landis. In an AVL Tree, the heights of the two child subtrees of any node differ by at most one, ensuring that the tree remains balanced. This balance is maintained through rotations during insertions and deletions, which ensures that the tree's height remains logarithmic relative to the number of nodes.

#### Key Properties
Self-Balancing: Ensures that the tree remains balanced after every insertion and deletion operation.
Height-Balanced: The difference in height between the left and right subtrees of any node is at most one.
Logarithmic Height: The height of an AVL Tree is O(log n), where n is the number of nodes, ensuring efficient search, insertion, and deletion operations.

## Project Structure
- **avl_tree.py**: Contains the implementation of the AVL Tree data structure.
- **LinkdList.py**: Contains the implementation of the Linked List data structure.
- **README.md**: This file, providing an overview of the project.
- **t_1.py**: Unit tests for the AVL Tree implementation.
- **t_2.py**: Unit tests for the Linked List implementation.
- **tester.py**: Script to run all tests.
## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/tamerabdalrazaq/AVL-LIST.git
    cd AVL-LIST
    ```

2. Install any required dependencies (if applicable).

### Running Tests

To run the tests, execute the following command:

```sh
python [tester.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Caverr%5C%5COneDrive%5C%5CDesktop%5C%5Cprojects%5C%5CAVL-LIST%5C%5Ctester.py%22%2C%22_sep%22%3A1%2C%22path%22%3A%22%2FC%3A%2FUsers%2Faverr%2FOneDrive%2FDesktop%2Fprojects%2FAVL-LIST%2Ftester.py%22%2C%22scheme%22%3A%22file%22%7D%7D)
```

## Usage
### AVL Tree
To use the AVL Tree, import the AVLTree class from avl_tree.py:

```sh
from avl_tree import AVLTree

# Example usage
avl = AVLTree()
avl.insert(10)
avl.insert(20)
avl.insert(30)
```

### Linked List
To use the Linked List, import the LinkedList class from LinkdList.py:

```sh
from LinkdList import LinkedList

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
```

#### Contributors
Tamer Abd Alrazaq (T)
Oday Saada (O)

#### License
This project is licensed under the MIT License - see the LICENSE file for details.
