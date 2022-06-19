


def binary_search(sequence, item):
    start_pos = 0
    end_pos = len(sequence) - 1 

    while start_pos <= end_pos:
        mid_pos = (start_pos + end_pos) // 2 
        if sequence[mid_pos] == item:
            return mid_pos
        elif sequence[mid_pos] < item:
            start_pos = mid_pos + 1
        else: 
            end_pos = mid_pos - 1 
    return None

test = binary_search([1,3,5,8,10,15,21,27], 3)

print(test)

