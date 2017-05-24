from linked_list import linked_list

if __name__ == '__main__':
    #Testing valid inputs
    print("Testing valid inputs")
    #Testing 3 types of initializing the linked list b,c,d as follows:
    #k > length of the linked list
    #k = 1, 2, 3 according to the lenght of the linked list
    #testing getData after adding node to the list with k = 3
    print("Testing simple valid input with linked list initialized default value")
    b= linked_list()
    b.add_Node(5)
    assert b.getData(5) == []
    assert b.getData(1) == [0,5]
    assert b.getData(2) == [5]
    assert b.getData(3) == []
    b.add_Node(7)
    assert b.getData(3) == [7]
    print("Done")
    print("Testing simple valid input with linked list initialized integer")
    c= linked_list(3)
    c.add_Node(5)
    assert c.getData(5) == []
    assert c.getData(1) == [3,5]
    assert c.getData(2) == [5]
    assert c.getData(3) == []
    c.add_Node(7)
    assert c.getData(3) == [7]
    print("Done")
    print("Testing simple valid input with linked list initialized list")
    d= linked_list([3,5])
    d.add_Node(5)
    assert d.getData(5) == []
    assert d.getData(1) == [3,5,5]
    assert d.getData(2) == [5,5]
    assert d.getData(3) == [5]
    d.add_Node(7)
    assert d.getData(3) == [5,7]
    print("Done")
    print("sting long lenght of linked list")
    a = linked_list(9)
    excepted = [9]
    for i in range(1000):
        a.add_Node(7)
        excepted.append(7)
    assert a.getData(1) == excepted
    assert a.getData(999) == [7,7,7]
    assert a.getData(1001) == [7]
    assert a.getData(1002) == []
    assert a.getData(2000) == []
    print("Done")
    print("Testing invalid inputs")
    #Testing invalid inputs
    assert d.getData(0) == [] 
    assert d.getData(-3) == []
    print("Done")
    print("All tests have been passed")

    
