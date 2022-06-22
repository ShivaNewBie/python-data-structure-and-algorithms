
#binary search is a faster way of finding the index position of a value in a list.


#it is required that the list should always be sorted.
def binary_search(sequence, item):
    sequence.sort()
    start_pos = 0 #get the first index 
    end_pos = len(sequence) - 1 #get last index 

    while start_pos <= end_pos: #we want to make sure that start_pos and end_pos index position would meet.
        mid_pos = (start_pos + end_pos) // 2 
        if sequence[mid_pos] == item: 
            return mid_pos
        elif sequence[mid_pos] < item: #we add plus one because we wanted to move on to the next index position. a visual representation https://stackoverflow.com/a/47256666
            start_pos = mid_pos
        else: 
            end_pos = mid_pos
    return None

test = binary_search([1,3,5,8,10,15,21,27], 21)

print(test)

