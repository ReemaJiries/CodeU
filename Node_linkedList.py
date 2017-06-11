class Node:
    def __init__(self, data = 0, parent_node = None, rightChild_node = None, leftChild_node = None):
        self._data = data
        self._parent = parent_node
        self._rightChild = rightChild_node
        self._leftChild = leftChild_node
    def setParent(self, parent_node):
        self._parent = parent_node
    def getParent(self):
        return self._parent
    def setLeftChild(self, leftChild_node):
        self._leftChild = leftChild_node
    def getLeftChild(self):
        return self._leftChild
    def setRightChild(self, rightChild_node):
        self._rightChild = rightChild_node
    def getRightChild(self):
        return self._rightChild
    def getData(self):
        return self._data
    def setData(self, data = 0): 
        self._data = data
