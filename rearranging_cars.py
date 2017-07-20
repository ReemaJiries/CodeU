from collections import OrderedDict

def rearranging_cars(old_parking, new_parking):
    """
    Input: two lists of the parking slots such as in every slot exist the number of the car from 0 to N-1.
    Where 0 is the empty slot.
    old_parking : the old positions
    new_parking : the new positions
    Output: list of tuples of needed moves such as every tuple is (from , to).
    """
    steps = []
    # the keys are the number of car and the values are the positions of the cars
    map_slot_cars = OrderedDict()
    
    for slot_index in range(len(old_parking)):
        car_num = old_parking[slot_index]
        map_slot_cars[car_num] = slot_index

    for new_slot_position in range(len(new_parking)):
        empty_park_position = map_slot_cars[0]
        new_park = new_parking[new_slot_position]
        old_park_position = map_slot_cars[new_park]        
        if new_slot_position != old_park_position and new_parking[new_slot_position] != 0:
            #checking if there is a need for an extra move of the wanted park in case it is full
            if new_slot_position != empty_park_position:
                old_parking[empty_park_position] = old_parking[new_slot_position]
                map_slot_cars[old_parking[new_slot_position]] = empty_park_position
                steps.append((new_slot_position, empty_park_position))
                
            old_parking[new_slot_position] = new_park
            old_parking[old_park_position] = 0
            map_slot_cars[new_park] = new_slot_position
            map_slot_cars[0] = old_park_position
            steps.append((old_park_position, new_slot_position))
        
    return steps


def print_rearranging_cars(steps):
    """
    printing the moves.
    """
    for step in steps:
        print ("move from " + str(step[0]) + " to " + str(step[1]))

if __name__ == '__main__':
    """
    Tests of new_parking function rearranging_cars
    """
    steps_result = rearranging_cars([1,2,0,3],[3,1,2,0])
    assert steps_result == [(0, 2), (3, 0), (1, 3), (2, 1), (3, 2)]
    steps_corner_test = rearranging_cars([3, 1, 2, 0], [0, 1, 2, 3])
    assert steps_corner_test == [(0,3)]
