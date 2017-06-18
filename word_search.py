class Dictionary:
    def isWord(self, word):
        """
        Input: word: string
        Returns whether the given string is a valid word.
        """
        pass

    def isPrefix(self, prefix):
        """
        Input: prefix: string
        Returns whether the given string is a prefix of at least one word in the dictionary. 
        """
        pass

def find_words_prefix(charecter,i,j,num_of_rows, num_of_columns, grid, dictionary,isVisit,valid_words ):
    """
    helper function filles valid_words according to the given inputs
    charecter - the charecter in the grid
    i,j - indexes of the character
    num_of_rows, num_of_columns: dims of the grid
    grid: the grid list of 2Dim. of characters
    dictionary: valid words
    isVisit1: list of 2 dim of bool type specify if we visit the character and check if exist valid path.
    valid_words: empty list - for the recursia (the output)
    """
    #passing over all adjacent cells of the given char
    x = max(0, i-1)
    y = max(0, j-1)
    if(dictionary.isWord(charecter)):
        valid_words.add(charecter)
    for x in range(max(0, i-1), min(i+2, num_of_rows)):
        for y in range(max(0, j-1), min(j+2, num_of_columns)):
            w = charecter + grid[x][y]
            if((x != i or y != j) and (isVisit[x][y] == False) and (dictionary.isPrefix(w))):
                isVisit[x][y] = True
                if(dictionary.isWord(w)):
                    valid_words.add(w)
                find_words_prefix(w,x,y,num_of_rows, num_of_columns, grid, dictionary, isVisit,valid_words)
 
def word_search(num_of_rows = 0, num_of_columns = 0, grid = [], dictionary = {}):
    """
    Input:
    num_of_rows , num_of_columns: the number of rows, number of columns.
    grid:a 2-dimensional array of characters (of the native char data type)
    and the dictionary
    output: valid words
    """
    valid_words = set()
    isVisit = []

    if num_of_rows is None or num_of_columns is None:
        print("Invalid Input: one of the inputs is None")
        return
    if num_of_rows is 0 or num_of_columns is 0 or grid == [[]] or dictionary == {} :
        print("Missing Input: missing one or more of the 4 required positional arguments")
        return
    if type(num_of_rows) != int or type(num_of_columns) != int:
        print("Invalid Input: num_of_rows or num_of_columns is not integer type")
        return
    if num_of_rows <= 0 or num_of_columns <= 0:
        print("Input Error: Invalid number of rows or columuns, it must be positive integers")
        return {}
    if (len(grid) < num_of_rows):
        print("Error: num of rows is large")
        return {}
    for r in range(num_of_rows):
        row = []
        for col in range(num_of_columns):
            row.append(False)
        isVisit.append(row)
    #passing over all possibale starting position at the grid
    for i in range(num_of_rows):
        if (len(grid[i]) < num_of_columns):
            print("Error: num of cols is large")
            return {}
        for j in range(num_of_columns):
            charecter = grid[i][j]
            if type(charecter) != str:
                print("Error: element not char type in the grid")
                return {}
            if charecter.isalpha() == False:
                print("Error: element not alpha type in the grid")
                return {}

            if (dictionary.isPrefix(charecter)):
                find_words_prefix(charecter,i,j,num_of_rows, num_of_columns, grid, dictionary, isVisit,valid_words)
                for r in range(num_of_rows):
                    for col in range(num_of_columns):
                        isVisit[r][col] = False
    return valid_words
if __name__ == '__main__':
    #Testing valid inputs
    print("Testing valid inputs:")
    print("Testing simple valid input")
    class Dictionary:
        def __init__(self, pa,da):
            self.k = pa
            self.p = da
        def isWord(self, word):
            for i in range(len(self.k)):
                if self.k[i] == word:
                    return True
            return False

        def isPrefix(self, prefix):
            for i in range(len(self.p)):
                if self.p[i] == prefix:
                    return True
            return False
    #tet1
    s = ["CAR", "CARD", "CART", "CAT"]
    p = ["C", "CA", "CAR", "CARD", "CART", "CAT"]
    d = Dictionary(s,p)
    l = word_search(2,3,[['A','A','R'],['T','C','D']],d)
    assert l == {'CAR', 'CARD', 'CAT'}
    #test2
    s = ["CAR", "CARD", "CART", "CAT"]
    p = ["C", "CA", "CAR", "CARD", "CART", "CAT"]
    d = Dictionary(s,p)
    l = word_search(2,2,[['A','R'],['C','D']],d)
    assert l == {'CAR', 'CARD'}
    print("Done\n")

    #Testing invalid inputs
    print("Testing invalid inputs:")
    #invalid dimention
    l = word_search(-2,3,[['A','A','R'],['T','C','D']],d)
    assert l == {}
    l = word_search("Ss",3,[['A','A','R'],['T','C','D']],d)
    assert l is None
    l = word_search("Ss",3,[['A','A','R'],['T','C','D']],d)
    assert l is None
    l = word_search("Ss",3,[['A','A','R'],['T','C','D']])
    assert l is None
    l = word_search(2,3,[['A',',','R'],['T','C','D']],d)
    assert l == {}
    l = word_search(2,3,[['A',5,'R'],['T','C','D']],d)
    assert l == {}
    l = word_search(10,3,[['A',5,'R'],['T','C','D']],d)
    assert l == {}
    print("Done\n")

    #Testing large input

    print("All tests have been passed")

