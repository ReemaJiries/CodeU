from Node import Node


class Binary_Tree():
    """
    the Binary Tree consist of Nodes with no duplicates keys and root node.
    constructor: accepts key of the root Node
    """
    def __init__(self, root_key = 0):
        if root_key == 0:
            self._root = None
            self._size = 0
        else:
            self._root = Node(root_key)
            self._size = 1

    def get_root(self):
        """returns the root node of binary tree"""
        return self._root

    
    def search(self,key, search_node = None):
        """
        Input:integer key in the array and optional start search node (the default is root Node)
        Output:the node with the given key
        """
        if search_node is None:
            search_node = self._root
        if search_node.getData() == key:
            return search_node
        if search_node.getLeftChild() and search_node.getRightChild():
            return self.search(key, search_node.getLeftChild()) or self.search(key, search_node.getRightChild())
        if search_node.getRightChild():
            return self.search(key, search_node.getRightChild())
        if search_node.getLeftChild():
            return self.search(key, search_node.getLeftChild())

    def add(self,key, parent_key = None, is_right = True):
        """
        Input: key of Integer type or Binary Tree, parent node key, boolean is_right
        is right child or left.
        Output: True or False.
        """
        if self._size == 0:
            self._root = Node(key)
        else:
            if type(key) is Binary_Tree:
                if  self.search(key.get_root().getData()):
                    print("Error: the given key {0} is exist in the Binar Tree".format(key.get_root().getData()))
                    return False
            elif isinstance(key,int):
                if self.search(key):
                    print("Error: the given key {0} is exist in the Binar Tree".format(key))
                    return False
            else:
                print("Error: the type of key isn't integer or Binary_Tree")
                return False
            temp_parent = self.search(parent_key, self._root)
            if isinstance(key,int):
                temp = Node(key, temp_parent)
            else:
                temp = key.get_root()
            if not is_right:
                if temp_parent.getLeftChild():
                    print("Error: the parent with the given key {0} had left child".format(key))
                    return False
                temp.setParent(temp_parent)
                temp_parent.setLeftChild(temp)
            else:
                if temp_parent.getRightChild():
                    print("Error: the parent with the given key {0} had right child".format(key))
                    return False
                temp.setParent(temp_parent)
                temp_parent.setRightChild(temp)
        self._size += 1
        return True
    
    
    def getAncestors(self, key):
        """
        Given a Binary Tree and a key, prints all the ancestors of the key in
        the given binary tree.
        Input: key of type Integer
        Output: list of all the ancestors of the key in the given binary tree
        """
        key_node = self.search(key)
        ancestors = []
        if key_node is None:
            print("Error: The key {0} is not exist in the Binary Tree".format(key))
            return ancestors
        if key == self._root.getData():
            return []
        while key_node.getParent() is not None:
            ancestors.append(key_node.getParent().getData())
            key_node = key_node.getParent()
        print(ancestors)
        return ancestors
    
    
    def commonAncestor(self, key1, key2):
        """
        Input: 2 Keys of type Integer
        Output: return he lowest common ancestor of two nodes in a binary tree
        """
        if self.search(key1) is None or self.search(key2) is None:
            print("Error: one of the given keys isn't exist in the BT")
            return []
        if key1 == self._root.getData() or key2 == self._root.getData():
            return self._root.getData()
        firstAncestors = self.getAncestors(key1)
        secondeAncestors = self.getAncestors(key2)
        if len(firstAncestors) == 0 or len(secondeAncestors) == 0:
            return
        else:
            if len(firstAncestors) <= len(secondeAncestors):
                if secondeAncestors[0] == key1:
                    return key1
                size = len(firstAncestors)
                for an in range(size):
                    if firstAncestors[an] in secondeAncestors:
                        return firstAncestors[an]
            else:
                if firstAncestors[0] == key2:
                    return key2
                size = len(firstAncestors)

                for an in range(size):
                    if secondeAncestors[an] in firstAncestors:
                        return secondeAncestors[an]
