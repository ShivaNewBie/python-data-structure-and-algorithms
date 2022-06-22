
def bubble_sort(L):
    swap = False
    while not swap:
        print('bubble sort: ' + str(L)) 
        swap = True
        for j in range(1, len(L)): 
            if L[j-1] > L[j]: #L[j-1] is the previous item L[j] would be the next or current item
                swap = False #no swap if L[j-1] > L[j]
                # temp = L[j] 
                # L[j] = L[j-1]
                # L[j-1] = temp 
            else:
                # temp = L[j] 
                L[j] = L[j-1] 
                L[j-1] = L[j]

testList = [1,3,5,7,2,6,25,18,13]

print('')
print(bubble_sort(testList))
print(testList)