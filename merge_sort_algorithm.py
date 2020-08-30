import random
import time


def random_numbers_generator():
    l = []
    for i in range(9):
        l.append(random.randint(0,9))
    return l

unsorted_l = random_numbers_generator()

start = time.time()

def merge(list, l, m, r):
    divider = m + 1
    l_cache = l
    out_list = []

    for i in range(r - l + 1):
        if l > m:
            out_list.append(list[divider])
            divider = divider + 1
        elif divider > r: # we would be out of the list when the divider is bigger than r
            out_list.append(list[l])
            l = l + 1
        elif list[l] < list[divider]:
            out_list.append(list[l]) # appending the smaller element to the new merge list
            l = l + 1 # moving to next element in the left part
        elif list[l] >= list[divider]:
            out_list.append(list[divider])
            divider = divider + 1 # have to move to the next element in the divider list

    for i in range(len(out_list)):
        list[i + l_cache] = out_list[i]


def merge_sort(unsorted_list, l = 0, r = None):
    if r is None:
        r = len(unsorted_list) - 1
    
    if l < r: # we only want the algorithm work if the left edge is smaller
        m = (l + r - 1) // 2 # defining the middle element of the list
        merge_sort(unsorted_list, l, m) # left part of the original list is sorted, using the list itself to work inplace
        merge_sort(unsorted_list, m + 1, r) # right part of the original list ist sorted
        merge(unsorted_list, l, m, r)

merge_sort(unsorted_l)
#print(unsorted_l)
end = time.time()
print(end - start) # checks the amount of time the algorithm needs to sort the list