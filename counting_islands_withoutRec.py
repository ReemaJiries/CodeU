num_of_rows = 0
num_of_columns = 0
realLenght = 0

        
def find_is_island(i,j, map_of_tiles,islands):
    """
    helper function find new exist island according to the given inputs
    i,j - indexes of the tile
    map_of_tiles: the map of tiles list of 2Dim. of booleans
    islands: valid islands
    """
    is_new_island = -1
    adjacents = [(max(0, i-1), j), (min(i+1, num_of_rows-1),j),(i, max(0, j-1)), (i, min(j+1, num_of_columns-1))]
    is_found = False
    
    #passing over all islands to find if the tile or one of it's djacents
    for island in islands:
        is_new_island += 1
        if (i,j) in island:
            is_found = True
            break
        for adjecent in adjacents:
            x = adjecent[0]
            y = adjecent[1]
            if map_of_tiles[x][y]:
                if (x,y) in island:
                    is_found = True
                    break;
                
    #new set of island
    if not is_found:
        new_one = set()
        indexs = (i,j)
        new_one.add(indexs)
        islands.append(new_one)
        is_new_island += 1

    #adding not exist  tiles to the set of the given tile
    for adjecent in adjacents:
        x = adjecent[0]
        y = adjecent[1]
        if map_of_tiles[x][y] and not (x == i and y == j):
            islands[is_new_island].add((x,y))


def check_inputs():
    """
    checking valid inputs
    """
    if num_of_rows is None or num_of_columns is None:
        print("Invalid Input: one of the inputs is None")
        return False
    if num_of_rows is 0 or num_of_columns is 0 :
        print("Missing Input: missing one or more of the 3 required positional arguments")
        return False
    if type(num_of_rows) != int or type(num_of_columns) != int:
        print("Invalid Input: num_of_rows or num_of_columns is not integer type")
        return False
    if num_of_rows <= 0 or num_of_columns <= 0:
        print("Input Error: Invalid number of rows or columuns, it must be positive integers")
        return False
    if realLenght < num_of_rows:
        print("Error: num of rows is large")
        return False
    return True


def find_number_of_islands(num_of_row = 0, num_of_column = 0, map_of_tiles = []):
    """
    num_of_rows , num_of_columns: the number of rows, number of columns.
    map_of_tiles:a 2-dimensional array of map of tiles. Each tile is either land(True) or water(False)
    output: number of islands
    """
    global num_of_rows
    global num_of_columns
    global realLenght
    realLenght = len(map_of_tiles)
    num_of_rows = num_of_row
    num_of_columns = num_of_column
    islands = []
    if not check_inputs():
        return 0
    i= 0
    j = 0
    islands = []
    #passing over all possibale starting position at the map
    while i != num_of_rows:
        if len(map_of_tiles[i]) < num_of_columns:
            print("Error: num of cols is large")
            return 0
        while j != num_of_columns:
            tile = map_of_tiles[i][j]
            if type(tile) != bool:
                print("Error: element not boolean type in the map")
                return 0
            if tile:
                find_is_island(i,j, map_of_tiles,islands)
            j += 1
        i += 1
        j = 0
    return len(islands)

        
if __name__ == '__main__':
    #Testing valid inputs
    print("Testing valid inputs:")
    print("Testing simple valid input")
    #tes1
    l = find_number_of_islands(4,4,[[False,True,False,True],[True,True,False,False],[False,False,True,False],[False,False,True,False]])
    assert l == 3
    #test2
    l2 = find_number_of_islands(1,4,[[True,True,True,True]])
    assert l2 == 1
    print("Done\n")

    #Testing invalid inputs
    print("Testing invalid inputs:")
    #invalid dimention
    l = find_number_of_islands(-2,4,[[False,True,False,True],[True,True,False,False],[False,False,True,False],[False,False,True,False]])
    assert l == 0
    l = find_number_of_islands("SS",4,[[False,True,False,True],[True,True,False,False],[False,False,True,False],[False,False,True,False]])
    assert l == 0
    l = find_number_of_islands(0,4,[[False,True,False,True],[True,True,False,False],[False,False,True,False],[False,False,True,False]])
    assert l == 0
    l = find_number_of_islands(None,4,[[False,True,False,True],[True,True,False,False],[False,False,True,False],[False,False,True,False]])
    assert l == 0
    l = find_number_of_islands(4,4,[[False,True,False,True],[None,True,False,False],[False,False,True,False],[False,False,True,False]])
    assert l == 0
    l = find_number_of_islands(4,4,[[False,True,5,True],[True,True,False,False],[False,False,True,False],[False,False,True,False]])
    assert l == 0
    l = find_number_of_islands(4,10,[[False,True,False,True],[True,True,False,False],[False,False,True,False],[False,False,True,False]])
    assert l == 0
    print("Done\n")

    #testing large inputs
    print("Testing large valid inputs:")
    large_map_False = [[False for i in range(1000)] for j in range(1000)]
    large_map_True = [[True for i in range(200)] for j in range(200)]
    large_map_TF = [[False if i%2 else True for i in range(20)] for j in range(20)]
    large_map_TF2 = [[False if i%2 and i%3 else True for i in range(18)] for j in range(18)]
    large_map_TF3 = [[False if i%3 else True for i in range(15)] for j in range(20)]
    l_f = find_number_of_islands(1000,1000, large_map_False)    
    assert l_f == 0
    l_t = find_number_of_islands(200,200, large_map_True)
    assert l_t == 1
    l_tf = find_number_of_islands(20,20, large_map_TF)
    assert l_tf == 10
    l_tf2 = find_number_of_islands(18,18, large_map_TF2)
    assert l_tf2 == 6
    l_tf3 = find_number_of_islands(20,15, large_map_TF3)
    assert l_tf3 == 5
    print("All tests have been passed")
    
    
