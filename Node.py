class Node:
    def __init__(self, data = 0):
        self._data = data
        self._next = None
    def setNext(self, next_node):
        self._next = next_node
    def getNext(self):
        return self._next
    def getData(self):
        return self._data
    def setData(self, data = 0): 
        self._data = data
