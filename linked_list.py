class linked_list:
    def __init__(self, data = 0):
        if type(data) is list:
            if len(data) <= 0:
                self._head = Node(0)
            else:
                self._head = Node(data[0])
                for num in range(1,len(data)):
                    if type(data[num]) is int:
                        self.add_Node(data[num])
                    else:
                        print("Invalid type: only integer type is acceptable")
        else:
            self._head = Node(data)
    def add_Node(self, data):
        if self._head.getNext() is None:
            newNode = Node(data)
            self._head.setNext(newNode)
        else:
            temp = self._head
            while temp.getNext() is not None:
                temp = temp.getNext()
            newNode = Node(data)
            temp.setNext(newNode)
    def changeNode(self, k, data):
        if k <= 0:
            return []
        temp = self._head
        i = 1
        while temp.getNext() is not None and i != -1:
            if i == k:
                temp.setData(data)
            temp = temp.getNext()
            i += 1
    def getData(self, k):
        if k <= 0:
            return []
        k_last_elements = []
        temp = self._head
        i = 1
        while temp.getNext() is not None:
            if i >= k:
                k_last_elements.append(temp.getData())
            temp = temp.getNext()
            i += 1
        k_last_elements.append(temp.getData())
        return k_last_elements
