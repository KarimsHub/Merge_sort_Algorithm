import random
import time


def random_numbers_generator():
    l = []
    for i in range(9):
        l.append(random.randint(0,9))
    return l

unsorted_l = random_numbers_generator()
print(unsorted_l)
start = time.time()

def merge(list, l, m, r):
    divider = m + 1 # to see there the right list starts
    l_cache = l # to see there the left has started
    out_list = []

    for i in range(r - l + 1): # sorting the amount of elemnts in our list
        if l > m:
            out_list.append(list[divider]) # there are no more elements in the left list
            divider = divider + 1
        elif divider > r: # we would be out of the list when the divider is bigger than r
            out_list.append(list[l]) # there are no more elements in the right list
            l = l + 1
        elif list[l] < list[divider]: # list[l] is first element of the left list and list[divider] the first element of the right list
            out_list.append(list[l]) # appending the smaller element to the new merge list
            l = l + 1 # moving to next element in the left part
        elif list[l] >= list[divider]:
            out_list.append(list[divider])
            divider = divider + 1 # have to move to the next element in the divider list

    for i in range(len(out_list)): # ierating through the elements of the already sorted outlist
        list[i + l_cache] = out_list[i]


def merge_sort(unsorted_list, l = 0, r = None): # setting the default values for l and r
    if r is None:
        r = len(unsorted_list) - 1 # have to use this workaround to set the lenght of the list as parameter
    
    if l < r: # we only want the algorithm work if the left edge is smaller
        m = (l + r - 1) // 2 # defining the middle element of the list
        merge_sort(unsorted_list, l, m) # using function on the left part of the unsorted list
        merge_sort(unsorted_list, m + 1, r) # using function on the right part of the unsorted list
        merge(unsorted_list, l, m, r) # using function to combine the parts 

merge_sort(unsorted_l)
#print(unsorted_l)
end = time.time()
print(end - start) # checks the amount of time the algorithm needs to sort the list