from Binary_Tree import Binary_Tree

if __name__ == '__main__':
    #Testing valid inputs
    print("Testing valid inputs")
    print("Testing simple valid input")
    bt = Binary_Tree()
    assert bt.add(5) == True
    assert bt.add(3,5) == True
    t = bt.search(5)
    assert bt.add(7,5,False) == True
    assert t.getData() == 5
    assert t.getRightChild().getData() == 3
    assert bt.add(2,3) == True
    assert bt.getAncestors(2) == [3,5]
    assert bt.add(1,3,False) == True
    assert bt.add(6,3,False) == False
    assert bt.add(9,3) == False
    assert bt.getAncestors(1) == [3,5]
    assert bt.getAncestors(2) == [3,5]
    #checking two childs
    assert bt.commonAncestor(1,2) == 3
    #checking parent and child
    assert bt.commonAncestor(2,3) == 3
    #checking left and left nodes
    assert bt.commonAncestor(1,7) == 5
    assert bt.add(8,2) == True
    #checking right and right nodes
    assert bt.commonAncestor(3,8) == 5
    #checking left and right nodes
    assert bt.commonAncestor(1,8) == 3
    assert bt.add(10,7,False) == True
    assert bt.getAncestors(10) == [7,5]
    assert bt.getAncestors(8) == [2,3,5]
    #checking right and left nodes
    assert bt.commonAncestor(10,8) == 5
    print("Done")
    
    print("sting long lenght of linked list")
    a = Binary_Tree()
    a.add(1001)
    excepted = []
    for i in range(500):
        if i == 0:
            a.add(i, 1001)
        else:
            a.add(i, i-1)
        excepted.append(500-i-1)
    a.add(i+1,i)
    excepted.append(1001)
    assert a.getAncestors(i+1) == excepted
    assert a.getAncestors(2) == [1,0,1001]
    assert a.getAncestors(10) == [9,8,7,6,5,4,3,2,1,0,1001]
    assert a.getAncestors(1001) == []
    assert a.getAncestors(0) == [1001]
    assert a.commonAncestor(1001,3) == 1001
    assert a.commonAncestor(499,50) == 49
    assert a.commonAncestor(499,0) == 1001  
    print("Done")
    print("Testing invalid inputs")
    #Testing invalid inputs
    assert a.getAncestors(-1) == []
    assert a.commonAncestor(1000, 9) == []
    print("Done")

    print("All tests have been passed")

    

