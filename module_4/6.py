'''
You need to write a function to implement the following game algorithm. The game function takes two arguments: a list of lists and an initial value power — the player's energy. Internal lists are lists with numerical energy values that the player can absorb if they are less than or equal to his energy. After absorbing a list item, the player moves along the list and either absorbs it completely to the end or, if he finds energy higher than his own, leaves it and moves on to the next list. At the end of the traversal of all lists, the function should return the total energy received by the player.

An example of a list:

[[1, 1, 5, 10], [10, 2], [1, 1, 1]]
For this list and an initial energy of 1, the player will absorb the first two values from the first list and leave it when he encounters the value 5, because at that moment he has an energy of 3. The second list will be skipped immediately, the third list will be completely absorbed and the final energy will be 6.
'''

def game(terra, power):
    for sublist in terra:
        for energy_value in sublist:
            if energy_value <= power:
                power += energy_value
            else:
                break

    return power
    
example_list = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
initial_power = 1
total_energy_received = game(example_list, initial_power)
print("Total energy received:", total_energy_received)