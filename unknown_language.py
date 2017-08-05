from collections import OrderedDict


class Graph:
    def __init__(self):
        """
        The Graph consist of ordered Vertices such as
        every slot in vertices will contain keys: alphabet and values: tree tuple type
        (isvisit,list of adj, degree)
        isvisit - mark the vertex as visited or no.
        list of adj - all vertices the consist edges in the graph such as v --> u
                    v character before u character at the language.
        degree - number of characters before v.            
        """
        self.vertices = OrderedDict()

    def add_Edge(self, v, u):
        """
        given v->u edge, adding all adjacents vertices u to v list of adj.
        """
        if v not in self.vertices.keys():    
            self.add_vertex(v)
        if u not in self.vertices.get(v)[1]:
            self.vertices.get(v)[1].append(u)
            self.vertices.get(v)[2] += 1

    def add_vertex(self, v):
        """
        add new valid vertex (character)
        """
        if v not in self.vertices.keys(): 
            self.vertices[v] = [False,[],0]
            

    def recTopologicalSort(self, v, allPaths):
        """
        recursive method to find the topological order of characters of the given language
        """       
        self.vertices.get(v)[0] = True
        adj = self.vertices.get(v)[1]
        for u in adj:
            if not self.vertices.get(u)[0]:
                self.recTopologicalSort(u,allPaths) 
        allPaths.append(v)

        
    def topologicalSort(self):
        """
        find the topological order of characters 
        """
        allPaths = []
        [self.recTopologicalSort(v,allPaths) for v in self.vertices if not self.vertices.get(v)[0]]
        
        return allPaths
    

def findAllTogiticalPaths(dictionary):
    """
    The main function that convert the problem of the dictionary to graph of vertices that represent
    the characters of the language and the edges are v --> u
    v character before u character at the language.
    after that finding the specific order using the topological order algorithm.
    """
    alphabet_graph = Graph()

    if len(dictionary) == 0:
        return []
    
    first_word = dictionary[0]    
    for v in first_word:
        alphabet_graph.add_vertex(v)
        
    for word_index in range(1,len(dictionary)):            
        word = dictionary[word_index]
        if word is None:
            print("Invalid Input: one of the inputs is None")
            return
        prev_word = dictionary[word_index-1]
        find_Adj_succ = False
        # try to get an edge between to characters in alphabet_graph from two adj words in the dict
        for v in range(len(word)):
            alphabet_graph.add_vertex(word[v])
            if not find_Adj_succ and len(word) <= len(prev_word):
                if word[v] is not prev_word[v]:
                    alphabet_graph.add_Edge(word[v], prev_word[v])
                    find_Adj_succ = True
    return alphabet_graph.topologicalSort()



if __name__ == '__main__':
    """
    Testing the findAllTogiticalPaths function
    """

    print("testing calling multiple times the findAllTogiticalPaths function:")
    for i in range(100):
        characters = findAllTogiticalPaths(["ART", "RAT", "CAT", "CAR"])
        assert ["A","T","R","C"] == characters or ["T","A","R","C"] == characters 
    print("Done\n")

    print("testing findAllTogiticalPaths function with diffrent valid input:")
    empty_characters = findAllTogiticalPaths([])
    assert [] == empty_characters

    characters = findAllTogiticalPaths(["ART", "RA", "CAT", "CAR"])
    assert ["A","T","R","C"] == characters or ["T","A","R","C"] == characters

    characters = findAllTogiticalPaths(["a", "b", "Ab", "Ac"])
    print(characters)
    assert ['a', 'b', 'c', 'A'] == characters or ['a', 'b', 'A', 'c'] == characters

    small_big_characters = findAllTogiticalPaths(["a","b","z","o", "A", "R", "CAT", "CAR"])
    assert ["a","b","z","o","A","T","R","C"] == small_big_characters 
    print("Done\n")
    
    print("Testing invalid inputs:")
    None_words = findAllTogiticalPaths(["a",None,"z","o", "A", "R", "CAT", "CAR"])
    assert None_words is None
    print("Done\n")

    print("All tests have been passed")
