
def data_preparation(list_data):
    new_list = []
    for element in list_data:
        if (len(element) > 2):
            new_list += sorted(element)[1:-1]
        else:
            new_list += element
            
    return sorted(new_list, reverse=True)

 
print(data_preparation(([1, 2,], [3], [5, 6, 2])))