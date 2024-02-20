'''
When analyzing data, it is often necessary to eliminate extreme values before working with the data further. Write a prepare_data function that removes the largest and smallest values from the given list, sorts it in ascending order, and returns the modified list.
'''
def prepare_data(data):
    return sorted(data)[1:-1]

print(prepare_data([3,2,5,1]))